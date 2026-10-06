import csv
from pathlib import Path
import sqlite3
import tempfile
import unittest

from threatintel.store import DataError, FIELDS, build, normalize_address, query, scan, source_urls


class StoreTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.case = self.root / "EVM" / "Sample"
        self.case.mkdir(parents=True)

    def write(self, rows, event_field="incident_date"):
        with (self.case / "addresses.csv").open("w", newline="", encoding="utf-8") as stream:
            writer = csv.DictWriter(stream, fieldnames=[event_field if f == "event_date" else f for f in FIELDS])
            writer.writeheader()
            writer.writerows(rows)

    def row(self, **changes):
        base = dict(case_id="TEST-2026-10-01", incident_date="2026-10-01", network="Ethereum", chain_id="1",
                    address="0x" + "A" * 40, indicator_type="wallet", entity="Unknown operator", role="proceeds",
                    source_confidence="high", control_confidence="unknown", attribution_scope="incident flow only",
                    monitoring="watch", priority="P1", threat_label="true", notes="Identity unresolved",
                    source="https://example.org/report | https://example.org/tx")
        base.update(changes)
        return base

    def test_build_query_preserves_evidence_and_chain_identity(self):
        same = "0x" + "A" * 40
        recovery = self.row(chain_id="56", network="BNB Smart Chain", address=same, indicator_type="recovery_wallet",
                            role="victim recovery", threat_label="false", priority="RECOVERY")
        self.write([self.row(), recovery])
        db = self.root / "out.sqlite"
        records, skipped = build(self.root, db)
        self.assertEqual((len(records), skipped), (2, []))
        results = query(db, address=same.lower())
        self.assertEqual({r["chain_id"] for r in results}, {"1", "56"})
        self.assertEqual(sum(r["threat_label"] for r in results), 1)
        self.assertEqual(len(results[0]["evidence_urls"]), 2)
        self.assertEqual(len(query(db, threat_only=True)), 1)
        with sqlite3.connect(db) as connection:
            self.assertEqual(connection.execute("SELECT count(*) FROM indicators").fetchone()[0], 2)
        with self.assertRaises(FileExistsError):
            build(self.root, db)

    def test_rejects_threat_labeled_recovery(self):
        self.write([self.row(indicator_type="recovery_wallet")])
        with self.assertRaisesRegex(DataError, "recovery/victim"):
            scan(self.root)

    def test_rejects_duplicate_case_indicator(self):
        self.write([self.row(), self.row(address="0x" + "a" * 40)])
        with self.assertRaisesRegex(DataError, "duplicate"):
            scan(self.root)

    def test_rejects_truncated_and_bad_sources(self):
        self.write([self.row(address="0xAbc…123")])
        with self.assertRaisesRegex(DataError, "truncated"):
            scan(self.root)
        self.write([self.row(source="not a URL")])
        with self.assertRaisesRegex(DataError, "http"):
            scan(self.root)

    def test_dates_and_btc_network_mapping(self):
        self.write([self.row(incident_date="2026-13-01")])
        with self.assertRaises(DataError):
            scan(self.root)
        self.write([self.row(network="Bitcoin", chain_id="", address="bc1qjkdzyt845q0vte6sax2nn9j40zdalec3q4zmrc")])
        record = scan(self.root)[0][0]
        self.assertEqual(record["chain_id"], "bitcoin-mainnet")
        self.assertEqual(record["chain_id_origin"], "network_mapping")

    def test_address_syntax_and_sources(self):
        self.assertEqual(normalize_address("1", "0x" + "A" * 40), "0x" + "a" * 40)
        with self.assertRaises(ValueError):
            normalize_address("solana-mainnet-beta", "7fTe…gRk7J")
        self.assertEqual(source_urls("https://a.test/x; https://b.test/y | https://a.test/x"),
                         ["https://a.test/x", "https://b.test/y"])

    def test_sweeps_and_legacy_are_reported_not_imported(self):
        self.write([self.row()])
        recap = self.root / "Multi-Chain" / "September-2026-Security-Sweep"
        recap.mkdir(parents=True)
        (recap / "addresses.csv").write_text("address,role\n0x123,victim\n")
        old = self.root / "TRON" / "Legacy"
        old.mkdir(parents=True)
        (old / "addresses.csv").write_text("address,role\nT123,victim\n")
        records, skipped = scan(self.root)
        self.assertEqual(len(records), 1)
        self.assertEqual(len(skipped), 2)


if __name__ == "__main__":
    unittest.main()
