#!/usr/bin/env python3

"""
FIND THE RATINGS FRONTIER

For example:

$ scripts/find_frontiers.py \
--scores testdata/synthetic_ratings.csv \
--metadata testdata/synthetic_scores_metadata.json \
--frontier output/test_frontier.json \
--no-debug

For documentation, type:

$ scripts/find_frontiers.py

TODO - Confirm this works visually

"""

import argparse
from argparse import ArgumentParser, Namespace
from typing import Any, List, Dict, Callable

import pandas as pd

from rdabase import require_args, read_json, write_json
from tradeoffs import scores_to_df, find_frontiers


def main() -> None:
    """Find the ratings frontier for the maps in an ensemble."""

    args: argparse.Namespace = parse_args()

    # Read the ratings from a score CSV

    fieldnames: List[str] = [
        "map",
        "proportionality",
        "competitiveness",
        "minority",
        "compactness",
        "splitting",
    ]
    fieldtypes: List[Callable] = [str, int, int, int, int, int]

    ratings: pd.DataFrame = scores_to_df(args.scores, fieldnames, fieldtypes)
    metadata: Dict[str, Any] = read_json(args.metadata)

    frontiers: Dict[str, Any] = find_frontiers(ratings, fieldnames)

    output: Dict[str, Any] = metadata
    output["frontiers"] = frontiers

    write_json(args.frontier, output)


def parse_args():
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Make a ratings table (CSV) for the notable maps in an ensemble."
    )

    parser.add_argument(
        "--scores",
        type=str,
        help="A CSV ensemble of scores including ratings to plot",
    )
    parser.add_argument(
        "--frontier",
        type=str,
        help="Frontier maps JSON file",
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
        "scores": "testdata/synthetic_ratings.csv",  # Only has map name & ratings
        "metadata": "testdata/synthetic_scores_metadata.json",
        "frontier": "output/test_frontier.json",
    }
    args = require_args(args, args.debug, debug_defaults)

    return args


if __name__ == "__main__":
    main()

### END ###