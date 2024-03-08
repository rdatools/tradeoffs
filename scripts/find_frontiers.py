#!/usr/bin/env python3

"""
FIND THE RATINGS FRONTIER

For example:

$ scripts/find_frontiers.py \
--scores ../../iCloud/fileout/ensembles/NC20C_scores.csv \
--metadata ../../iCloud/fileout/ensembles/NC20C_scores_metadata.json \
--frontier ../../iCloud/fileout/ensembles/NC20C_frontiers.json \
--verbose \
--no-debug

For documentation, type:

$ scripts/find_frontiers.py
"""

import argparse
from argparse import ArgumentParser, Namespace
from typing import Any, List, Dict, Tuple, Set, Callable

import warnings

warnings.warn = lambda *args, **kwargs: None

import pandas as pd
import itertools

from rdabase import require_args, read_json, write_json
from rdaensemble.general import ratings_dimensions
from tradeoffs import (
    scores_to_df,
    read_ratings,
    find_frontiers,
    is_pareto_efficient_value,
    id_most_notable_maps,
)


def main() -> None:
    """Find the ratings frontier for the maps in an ensemble."""

    args: argparse.Namespace = parse_args()

    # Read the ratings from a score CSV

    fieldnames: List[str] = ["map"] + ratings_dimensions
    fieldtypes: List[Callable] = [str, int, int, int, int, int]

    ratings_df: pd.DataFrame = scores_to_df(
        args.scores,
        fieldnames,
        fieldtypes,
        filter=True,
        verbose=args.verbose,
    )
    ratings: List[Dict] = read_ratings(
        args.scores,
        verbose=args.verbose,
    )
    metadata: Dict[str, Any] = read_json(args.metadata)

    frontiers: Dict[str, Any] = find_frontiers(
        ratings_df, is_pareto_efficient_value, verbose=args.verbose
    )
    # indices: List[Dict[str, Dict[str, str | int]]] = id_most_notable_maps(frontiers)

    output: Dict[str, Any] = metadata
    output["frontiers"] = frontiers
    # output["notable_maps"] = indices

    #

    zones: Dict[str, List[str]] = {}
    frontier_points: Dict[str, Set[Tuple[int, int]]] = {}
    for k, v in frontiers.items():
        zones[k] = []
        frontier_points[k] = set()

        pair: List[str] = k.split("_")
        ydim: str = pair[0]
        xdim: str = pair[1]
        d1: int = ratings_dimensions.index(ydim)
        d2: int = ratings_dimensions.index(xdim)

        for m in v:
            # zones[k].append(m["map"])
            x: int = m["ratings"][d2]
            y: int = m["ratings"][d1]
            frontier_points[k].add((x, y))

    # TODO - Find the plans in the zone
    # For each plan in ratings:
    #     For each frontier (pair of dimensions:
    #         Get the pair of ratings
    #         If they are "near" any frontier point, add it to that zone
    # Print # of frontier points
    # Print # of zone points

    #

    output["zones"] = zones

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
        "scores": "../../iCloud/fileout/ensembles/NC20C_scores.csv",
        "metadata": "../../iCloud/fileout/ensembles/NC20C_scores_metadata.json",
        "frontier": "~/Downloads/test_frontier.json",
        "verbose": True,
    }
    args = require_args(args, args.debug, debug_defaults)

    return args


if __name__ == "__main__":
    main()

### END ###
