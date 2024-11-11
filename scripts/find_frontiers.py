#!/usr/bin/env python3

"""
FIND THE RATINGS FRONTIER

For example, see the workflows directory.

For documentation, type:

$ scripts/find_frontiers.py -h

"""

import argparse
from argparse import ArgumentParser, Namespace
from typing import Any, List, Dict, Callable

import warnings

warnings.warn = lambda *args, **kwargs: None

import pandas as pd
import itertools

from rdabase import require_args, read_json, write_json
from rdaensemble.general import ratings_dimensions
from tradeoffs import (
    scores_to_df,
    find_frontiers,
    is_pareto_efficient_value,
)


def main() -> None:
    """Find the ratings frontier for the maps in an ensemble."""

    args: argparse.Namespace = parse_args()

    filter: bool = not args.nofilter

    # Read the ratings from a score CSV

    fieldnames: List[str] = ["map"] + ratings_dimensions
    fieldtypes: List[Callable] = [str, int, int, int, int, int]

    ratings: pd.DataFrame = scores_to_df(
        args.scores,
        fieldnames,
        fieldtypes,
        filter=filter,
        roughly_equal=args.roughlyequal,
        verbose=args.verbose,
    )
    metadata: Dict[str, Any] = read_json(args.metadata)

    frontiers: Dict[str, Any] = find_frontiers(
        ratings, is_pareto_efficient_value, verbose=args.verbose
    )

    output: Dict[str, Any] = metadata
    output["frontiers"] = frontiers

    if args.verbose:
        ratings_pairs: List = list(itertools.combinations(ratings_dimensions, 2))

        total_points: int = 0
        for i, f in enumerate(ratings_pairs):
            frontier_key: str = f"{f[0]}_{f[1]}"
            points: int = len(frontiers[frontier_key])
            total_points += points
            print(f"{i} - The {frontier_key} frontier involves {points} plans.")

        print()
        print(f"Altogether there are {total_points} plans on frontiers.")
        print()

    if not args.debug:
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
        "--roughlyequal",
        type=float,
        default=0.01,
        help="'Roughly equal' population threshold",
    )
    parser.add_argument(
        "--metadata",
        type=str,
        help="Metadata JSON for the scoring CSV",
    )
    parser.add_argument(
        "--frontier",
        type=str,
        help="Frontier maps JSON file",
    )
    parser.add_argument(
        "--nofilter", dest="nofilter", action="store_true", help="Don't filter plans"
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
        "scores": "../../temp/tradeoffs/NC/ensembles/NC20C_scores_augmented.csv",
        "metadata": "../../temp/tradeoffs/NC/ensembles/NC20C_scores_optimized_metadata.json",
        "frontier": "../../temp/tradeoffs/NC/ensembles/NC20C_frontiers_optimized.json",
        "verbose": True,
    }
    args = require_args(args, args.debug, debug_defaults)

    return args


if __name__ == "__main__":
    main()

### END ###
