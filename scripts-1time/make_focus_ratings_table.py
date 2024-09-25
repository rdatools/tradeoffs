#!/usr/bin/env python3

"""
MAKE A RATINGS TABLE (CSV) FOR DRA OFFICIAL MAPS

For example:

$ scripts-1time/make_focus_ratings_table.py --state AL --plantype Lower

For documentation, type:

$ scripts/make_focus_ratings_table.py -h

"""

import argparse
from argparse import ArgumentParser, Namespace

from typing import Any, List, Dict

from rdabase import cycle, yyyy, require_args, read_json, write_csv


def main() -> None:
    """Make a ratings table (CSV) for the official maps copied from DRA."""

    args: argparse.Namespace = parse_args()

    xx: str = args.state
    plan_type: str = args.plantype
    prefix: str = f"{args.state}{cycle[2:]}{plan_type[0]}"
    output: str = f"{args.output}/{prefix}_focus_scores.csv"

    if args.verbose:
        print(f"Making {xx}/{plan_type} ratings table in {output} ...")

    #

    file_names: List[str] = [
        "official",
    ]

    dims_to_dims: Dict[str, str] = {
        "proportionality": "score_proportionality",
        "competitiveness": "score_competitiveness",
        "minority": "score_minorityRights",
        "compactness": "score_compactness",
        "splitting": "score_splitting",
    }

    cols: List[str] = [
        "proportionality",
        "competitiveness",
        "minority",
        "compactness",
        "splitting",
    ]
    labels: List[str] = [
        f"Official {yyyy}",
    ]
    name_to_label: Dict[str, str] = dict(zip(file_names, labels))

    #

    try:
        rows: List[Dict[str, Any]] = []

        for notable_dim in file_names:
            pulled_ratings: str = (
                f"{args.input}/{xx}_{yyyy}_{plan_type.capitalize()}_{notable_dim.capitalize()}_ratings.json"
            )
            data: Dict[str, Any] = read_json(pulled_ratings)

            row: Dict[str, Any] = {}
            row["MAP"] = name_to_label[notable_dim]

            ratings: Dict[str, Any] = {
                to_dim.upper(): data[from_key]
                for to_dim, from_key in dims_to_dims.items()
            }
            row.update(ratings)

            rows.append(row)

        write_csv(output, rows, ["MAP"] + [c.upper() for c in cols])

    except Exception as e:
        print(f"Error: {e}")

    pass


def parse_args():
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Make a ratings table (CSV) for the notable maps for a state & type of plan."
    )

    parser.add_argument(
        "--state",
        help="The two-character state code (e.g., NC)",
        type=str,
    )
    parser.add_argument(
        "--plantype",
        help="The type of plan (congress, upper, lower)",
        type=str,
    )
    parser.add_argument(
        "--input",
        type=str,
        default="intermediate",
        help="The directory where the ratings JSONs were saved",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="intermediate",
        help="The directory where the CSV should be saved",
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
        "state": "AL",
        "plantype": "Lower",
        "input": "intermediate",
        "output": "intermediate",
    }
    args = require_args(args, args.debug, debug_defaults)

    return args


if __name__ == "__main__":
    main()

### END ###
