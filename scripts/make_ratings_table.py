#!/usr/bin/env python3

"""
MAKE RATINGS TABLE (CSV)

For example, see the workflows directory.

For documentation, type:

$ scripts/make_ratings_table.py -h

"""

import argparse
from argparse import ArgumentParser, Namespace

from typing import Any, List, Dict, Callable

import warnings

warnings.warn = lambda *args, **kwargs: None

import pandas as pd

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
    labels: List[str] = [
        "Most Proportional",
        "Most Competitive",
        "Best Minority",
        "Most Compact",
        "Least Splitting",
    ]
    name_to_label: Dict[str, str] = dict(zip(cols, labels))

    rows: List[Dict[str, Any]] = []

    for m in data["notable_maps"]:
        name: str = list(m.keys())[0]
        ratings: Dict[str, int] = dict(zip([c.upper() for c in cols], m["ratings"]))

        row: Dict[str, Any] = {}
        row["MAP"] = name_to_label[name]
        row["ID"] = m[name]
        row.update(ratings)

        rows.append(row)

    write_csv(args.output, rows, ["MAP", "ID"] + [c.upper() for c in cols])


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
        "notables": "testdata/test_notable_maps.json",
        "output": "output/test_ratings.csv",
    }
    args = require_args(args, args.debug, debug_defaults)

    return args


if __name__ == "__main__":
    main()

### END ###
