#!/usr/bin/env python3

"""
MAKE RATINGS TABLE (CSV)

For example:

$ scripts/make_ratings_table.py \
--notables ~/iCloud/fileout/ensembles/NC20C_RMfRST_1000_notables_maps.json \
--output output/test_ratings.csv \
--no-debug

For documentation, type:

$ scripts/make_ratings_table.py

"""

import argparse
from argparse import ArgumentParser, Namespace

from typing import Any, List, Dict

from rdabase import require_args, read_json, write_csv


def main() -> None:
    """Make a ratings table (CSV) for the notable maps in an ensemble."""

    args: argparse.Namespace = parse_args()

    data: Dict[str, Any] = read_json(args.notables)
    cols: List[str] = [
        "proportionality",
        "competitiveness",
        "minority",
        "compactness",
        "splitting",
    ]

    rows: List[Dict[str, Any]] = list()
    for m in data["notable_maps"]:
        name: str = list(m.keys())[0]
        ratings: Dict[str, int] = dict(zip([c.upper() for c in cols], m["ratings"]))

        row: Dict[str, Any] = dict()
        row["MAP"] = m[name]
        row.update(ratings)

        rows.append(row)

    write_csv(args.output, rows, ["MAP"] + [c.upper() for c in cols])


def parse_args():
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Make a ratings table (CSV) for the notable maps in an ensemble."
    )

    parser.add_argument(
        "--notables",
        type=str,
        help="The notable maps JSON file",
    )
    parser.add_argument(
        "--output",
        type=str,
        help="The CSV file to write the ratings to",
    )

    parser.add_argument(
        "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
    )

    # Enable debug/explicit mode
    parser.add_argument("--debug", default=True, action="store_true", help="Debug mode")
    parser.add_argument(
        "--no-debug", dest="debug", action="store_false", help="Explicit mode"
    )

    args: Namespace = parser.parse_args()

    # Default values for args in debug mode
    debug_defaults: Dict[str, Any] = {
        "notables": "testdata/synthetic_notables_maps.json",
        "output": "output/test_ratings.csv",
    }
    args = require_args(args, args.debug, debug_defaults)

    return args


if __name__ == "__main__":
    main()

### END ###