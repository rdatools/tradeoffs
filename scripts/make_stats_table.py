#!/usr/bin/env python3

"""
MAKE STATISTICS TABLE

For example, see the workflows directory.

For documentation, type:

$ scripts/make_stats_table.py -h

"""

import argparse
from argparse import ArgumentParser, Namespace

from typing import List, Dict, Any, Callable

import warnings

warnings.warn = lambda *args, **kwargs: None

import math
import pandas as pd

from rdabase import require_args, write_csv
from rdaensemble.general import ratings_dimensions

from tradeoffs import scores_to_df


def main() -> None:
    """Collect statistics for the ratings for the plans in an ensemble."""

    args: argparse.Namespace = parse_args()
    filter: bool = not args.nofilter

    fieldnames: List[str] = ["map"] + ratings_dimensions
    fieldtypes: List[Callable] = [str, int, int, int, int, int]

    df: pd.DataFrame = scores_to_df(
        args.scores,
        fieldnames,
        fieldtypes,
        roughly_equal=args.roughlyequal,
        filter=filter,
    )

    cols: List[str] = ["count", "mean", "std", "min", "25%", "50%", "75%", "max"]
    rows: List[Dict[str, Any]] = []
    for dimension in ratings_dimensions:
        df_stats: Dict = df[dimension].describe().to_dict()
        stats: Dict = {}

        for k, v in df_stats.items():
            # stats[k.upper()] = int(v) if k != "std" else v
            if v is None or math.isnan(v):
                stats[k.upper()] = None
            elif k == "std":
                stats[k.upper()] = v
            else:
                stats[k.upper()] = int(v)

        row: Dict[str, Any] = {}
        row["DIMENSION"] = dimension.capitalize()
        row.update(stats)
        rows.append(row)

    write_csv(args.output, rows, ["DIMENSION"] + [c.upper() for c in cols])


def parse_args():
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Make historgrams for the ratings for the plans in an ensemble."
    )

    parser.add_argument(
        "--scores",
        type=str,
        help="A CSV ensemble of scores including ratings to plot",
    )
    parser.add_argument(
        "--roughlyequal",
        type=float,
        default=0.01,
        help="'Roughly equal' population threshold",
    )
    parser.add_argument(
        "--nofilter", dest="nofilter", action="store_true", help="Don't filter plans"
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
        # "scores": "../../temp/tradeoffs/NC/ensembles/NC20C_scores.csv",
        "scores": "../../temp/tradeoffs/NC/ensembles-upper/NC20U_scores.csv",
        # "output": "../../temp/tradeoffs/NC/docs/_data/NC20C_statistics.csv",
        "output": "temp/NC20U_statistics.csv",
    }
    args = require_args(args, args.debug, debug_defaults)

    return args


if __name__ == "__main__":
    main()

### END ###
