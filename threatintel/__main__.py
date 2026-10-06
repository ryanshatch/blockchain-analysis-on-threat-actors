"""CLI for reproducible local dataset checks and queries."""

import argparse
import json
from pathlib import Path
import sys

from .store import DataError, build, query, scan


def main(argv=None):
    parser = argparse.ArgumentParser(description="Validate and query dedicated case address records without changing their CSV sources")
    commands = parser.add_subparsers(dest="command", required=True)
    validate = commands.add_parser("validate", help="audit supported rows and list skipped legacy files")
    validate.add_argument("--root", type=Path, default=Path("."))
    generate = commands.add_parser("build", help="create a derived SQLite file (never overwrite)")
    generate.add_argument("--root", type=Path, default=Path("."))
    generate.add_argument("--output", type=Path, required=True)
    lookup = commands.add_parser("query", help="return evidence-aware JSON observations")
    lookup.add_argument("--db", type=Path, required=True)
    lookup.add_argument("--address")
    lookup.add_argument("--case")
    lookup.add_argument("--threat-only", action="store_true")
    lookup.add_argument("--limit", type=int, default=100)
    args = parser.parse_args(argv)
    try:
        if args.command == "query":
            if not 1 <= args.limit <= 1000:
                parser.error("--limit must be between 1 and 1000")
            print(json.dumps(query(args.db, args.address, args.case, args.threat_only, args.limit), indent=2))
            return 0
        records, skipped = scan(args.root) if args.command == "validate" else build(args.root, args.output)
        print(json.dumps({"cases": len({r["case_id"] for r in records}), "observations": len(records),
                          "skipped_files": [{"file": path, "reason": reason} for path, reason in skipped]}, indent=2))
        return 0
    except (DataError, FileExistsError, FileNotFoundError, OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
