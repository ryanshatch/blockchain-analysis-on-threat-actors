"""Validate dedicated case indicators and build a derived SQLite index.

CSV files remain the source of truth. No network calls or automatic attribution
are performed by this module.
"""

import csv
import os
from pathlib import Path
import re
import sqlite3
import tempfile
from datetime import date
from urllib.parse import urlsplit

FIELDS = (
    "case_id", "event_date", "network", "chain_id", "address",
    "indicator_type", "entity", "role", "source_confidence",
    "control_confidence", "attribution_scope", "monitoring", "priority",
    "threat_label", "notes", "source",
)
EVM = re.compile(r"0x[0-9a-fA-F]{40}\Z")
BTC = re.compile(r"(?:bc1[ac-hj-np-z02-9]{11,87}|[13][1-9A-HJ-NP-Za-km-z]{25,34})\Z", re.I)
SOL = re.compile(r"[1-9A-HJ-NP-Za-km-z]{32,44}\Z")
TRON = re.compile(r"T[1-9A-HJ-NP-Za-km-z]{33}\Z")
EVM_CHAINS = {"1", "56", "137", "42161", "43114", "8453", "10", "250", "sonic-mainnet", "cronos-mainnet"}
PROTECTED_TYPES = {"recovery_wallet", "victim_wallet", "victim_contract", "victim_program"}


class DataError(ValueError):
    """Invalid source row with a file and line number in its message."""


def source_urls(raw):
    urls = [part.strip() for part in re.split(r"\s*[|;]\s*", raw) if part.strip()]
    if not urls or any(urlsplit(url).scheme not in {"http", "https"} or not urlsplit(url).netloc for url in urls):
        raise ValueError("source must contain one or more http(s) evidence URLs")
    return list(dict.fromkeys(urls))


def normalize_address(chain_id, address):
    if not address or address != address.strip() or "…" in address or "..." in address:
        raise ValueError("address is empty, truncated, or has surrounding whitespace")
    if chain_id in EVM_CHAINS or chain_id.isdigit():
        if not EVM.fullmatch(address):
            raise ValueError("expected a complete 0x-prefixed EVM address")
        return address.lower()
    if chain_id == "bitcoin-mainnet":
        if not BTC.fullmatch(address):
            raise ValueError("expected a complete Bitcoin mainnet address")
        return address.lower() if address.lower().startswith("bc1") else address
    if chain_id == "solana-mainnet-beta":
        if not SOL.fullmatch(address):
            raise ValueError("expected a complete Solana base58 address")
        return address
    if chain_id == "tron-mainnet":
        if not TRON.fullmatch(address):
            raise ValueError("expected a complete TRON base58 address")
        return address
    # Other networks retain exact identifiers rather than pretending an EVM rule fits.
    if len(address) > 128 or any(ch.isspace() for ch in address):
        raise ValueError("invalid unsupported-network identifier")
    return address


def parse_row(row, file, line, event_field):
    loc = f"{file}:{line}"
    try:
        if None in row or any(v is None for v in row.values()):
            raise ValueError("CSV row does not match its header")
        record = {key: row[key].strip() for key in FIELDS if key != "event_date"}
        record["event_date"] = row[event_field].strip()
        for key in ("case_id", "network", "address", "indicator_type", "entity", "role", "source_confidence", "attribution_scope", "priority"):
            if not record[key]:
                raise ValueError(f"{key} is required")
        record["chain_id_origin"] = "source"
        if not record["chain_id"] and record["network"] == "Bitcoin":
            # Six older COLDCARD rows identify Bitcoin but omit their chain ID.
            record["chain_id"] = "bitcoin-mainnet"
            record["chain_id_origin"] = "network_mapping"
        if not record["chain_id"]:
            raise ValueError("chain_id is required; only Bitcoin has an explicit legacy mapping")
        if record["event_date"]:
            date.fromisoformat(record["event_date"])
        if record["threat_label"] not in {"true", "false"}:
            raise ValueError("threat_label must be true or false")
        if record["indicator_type"].lower().replace(" ", "_") in PROTECTED_TYPES and record["threat_label"] == "true":
            raise ValueError("recovery/victim infrastructure cannot be threat-labeled")
        record["address_key"] = normalize_address(record["chain_id"], record["address"])
        record["sources"] = source_urls(record["source"])
        record["source_file"] = file.as_posix()
        record["source_line"] = line
        return record
    except (ValueError, KeyError) as exc:
        raise DataError(f"{loc}: {exc}") from exc


def scan(root):
    """Yield normalized records and explicit unsupported-file paths."""
    records, skipped = [], []
    seen = set()
    for path in sorted(root.rglob("addresses.csv")):
        relative = path.relative_to(root)
        # Sweep files recap dedicated cases and would inflate an incident count.
        if "Security-Sweep" in str(relative) or "security-sweep" in str(relative).lower():
            skipped.append((str(relative), "recap/sweep; avoid duplicate evidence"))
            continue
        with path.open(newline="", encoding="utf-8-sig") as stream:
            reader = csv.DictReader(stream)
            header = reader.fieldnames or []
            event_fields = [key for key in ("incident_date", "disclosure_date", "observed_date") if key in header]
            expected = (set(FIELDS) - {"event_date"}) | set(event_fields)
            if len(event_fields) != 1 or len(header) != len(expected) or set(header) != expected:
                skipped.append((str(relative), "legacy/unsupported column schema"))
                continue
            for row in reader:
                if not any(value for value in row.values() if isinstance(value, str)):
                    continue
                record = parse_row(row, relative, reader.line_num, event_fields[0])
                key = (record["case_id"], record["chain_id"], record["address_key"], record["indicator_type"])
                if key in seen:
                    raise DataError(f"{relative}:{reader.line_num}: duplicate case/network/indicator identifier")
                seen.add(key)
                records.append(record)
    return records, skipped


SCHEMA = """
PRAGMA foreign_keys = ON;
CREATE TABLE cases (
    case_id TEXT PRIMARY KEY,
    entity TEXT NOT NULL,
    case_file TEXT NOT NULL
);
CREATE TABLE indicators (
    indicator_id INTEGER PRIMARY KEY,
    chain_id TEXT NOT NULL,
    address_key TEXT NOT NULL,
    address TEXT NOT NULL,
    indicator_type TEXT NOT NULL,
    UNIQUE(chain_id, address_key, indicator_type)
);
CREATE TABLE observations (
    observation_id INTEGER PRIMARY KEY,
    case_id TEXT NOT NULL REFERENCES cases(case_id),
    indicator_id INTEGER NOT NULL REFERENCES indicators(indicator_id),
    event_date TEXT,
    network TEXT NOT NULL,
    role TEXT NOT NULL,
    source_confidence TEXT NOT NULL,
    control_confidence TEXT NOT NULL,
    attribution_scope TEXT NOT NULL,
    monitoring TEXT NOT NULL,
    priority TEXT NOT NULL,
    threat_label INTEGER NOT NULL CHECK(threat_label IN (0,1)),
    notes TEXT NOT NULL,
    source_file TEXT NOT NULL,
    source_line INTEGER NOT NULL,
    chain_id_origin TEXT NOT NULL CHECK(chain_id_origin IN ('source','network_mapping')),
    UNIQUE(case_id, indicator_id)
);
CREATE TABLE evidence (
    observation_id INTEGER NOT NULL REFERENCES observations(observation_id),
    url TEXT NOT NULL,
    PRIMARY KEY(observation_id, url)
);
CREATE INDEX observation_indicator ON observations(indicator_id);
CREATE INDEX observation_priority ON observations(priority, threat_label);
"""


def build(root, output):
    root, output = Path(root).resolve(), Path(output).resolve()
    records, skipped = scan(root)
    if not records:
        raise DataError("no compatible dedicated case indicators found")
    if output.exists():
        raise FileExistsError(f"{output} exists; choose a new output path")
    if not output.parent.is_dir():
        raise FileNotFoundError(f"output parent does not exist: {output.parent}")
    fd, temporary = tempfile.mkstemp(prefix=".threatintel-", suffix=".sqlite", dir=output.parent)
    os.close(fd)
    try:
        with sqlite3.connect(temporary) as db:
            db.executescript(SCHEMA)
            for r in records:
                case_file = str(Path(r["source_file"]).parent / "README.md")
                db.execute("INSERT OR IGNORE INTO cases VALUES(?,?,?)", (r["case_id"], r["entity"], case_file))
                db.execute("INSERT OR IGNORE INTO indicators(chain_id,address_key,address,indicator_type) VALUES(?,?,?,?)",
                           (r["chain_id"], r["address_key"], r["address"], r["indicator_type"]))
                indicator_id = db.execute("SELECT indicator_id FROM indicators WHERE chain_id=? AND address_key=? AND indicator_type=?",
                                          (r["chain_id"], r["address_key"], r["indicator_type"])).fetchone()[0]
                cursor = db.execute("""INSERT INTO observations(case_id,indicator_id,event_date,network,role,source_confidence,
                    control_confidence,attribution_scope,monitoring,priority,threat_label,notes,source_file,source_line,
                    chain_id_origin) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", (r["case_id"], indicator_id, r["event_date"] or None,
                    r["network"], r["role"], r["source_confidence"], r["control_confidence"],
                    r["attribution_scope"], r["monitoring"], r["priority"], r["threat_label"] == "true",
                    r["notes"], r["source_file"], r["source_line"], r["chain_id_origin"]))
                db.executemany("INSERT INTO evidence VALUES(?,?)", ((cursor.lastrowid, url) for url in r["sources"]))
            if db.execute("PRAGMA foreign_key_check").fetchone():
                raise DataError("SQLite foreign-key integrity check failed")
        os.link(temporary, output)  # fails rather than replacing a file created concurrently
    finally:
        os.unlink(temporary)
    return records, skipped


def query(db_path, address=None, case_id=None, threat_only=False, limit=100):
    clauses, args = [], []
    if address:
        clauses.append("(i.address_key=? OR i.address=?)")
        args.extend((address.lower() if address.startswith("0x") or address.lower().startswith("bc1") else address, address))
    if case_id:
        clauses.append("o.case_id=?")
        args.append(case_id)
    if threat_only:
        clauses.append("o.threat_label=1")
    where = " WHERE " + " AND ".join(clauses) if clauses else ""
    statement = """SELECT o.case_id,c.entity,i.chain_id,i.address,i.indicator_type,o.event_date,o.network,
        o.role,o.source_confidence,o.control_confidence,o.attribution_scope,o.monitoring,o.priority,
        o.threat_label,o.notes,o.source_file,o.source_line,o.chain_id_origin,o.observation_id
        FROM observations o JOIN indicators i USING(indicator_id) JOIN cases c USING(case_id)""" + where + " ORDER BY o.case_id,i.chain_id,i.address LIMIT ?"
    with sqlite3.connect(f"file:{Path(db_path).resolve()}?mode=ro", uri=True) as db:
        db.row_factory = sqlite3.Row
        results = []
        for row in db.execute(statement, (*args, limit)):
            item = dict(row)
            item["threat_label"] = bool(item["threat_label"])
            evidence = db.execute("SELECT url FROM evidence WHERE observation_id=? ORDER BY url", (item.pop("observation_id"),))
            item["evidence_urls"] = [url for (url,) in evidence]
            results.append(item)
        return results
