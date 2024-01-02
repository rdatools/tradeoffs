#!/usr/bin/env python3

"""
FIND THE RATINGS FRONTIER

For example:

$ scripts/find_frontier.py \
--scores testdata/synthetic_ratings.csv \
--frontier output/test_frontier.json \
--no-debug

For documentation, type:

$ scripts/find_frontier.py
"""

import argparse
from argparse import ArgumentParser, Namespace
from typing import Any, List, Dict, Callable

from csv import DictReader
import pandas as pd
import numpy as np
import itertools

from rdabase import require_args, write_json
from tradeoffs import scores_to_df


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
    pairs: List = list(itertools.combinations(fieldnames[1:], 2))
    frontiers: Dict[str, Any] = dict()

    for p in pairs:
        label: str = f"{p[0]}_{p[1]}"
        frontiers[label] = list()

        subset: pd.DataFrame = ratings[list(p)]
        is_frontier: np.ndarray = is_pareto_efficient_dumb(subset.to_numpy())

        maps: List[str] = list()
        for i, is_efficient in enumerate(is_frontier):
            if is_efficient:
                maps.append(ratings.iloc[i]["map"])

        for m in maps:
            point = (
                ratings.loc[ratings["map"] == m, fieldnames].values.flatten().tolist()
            )
            frontiers[label].append(point)

    output: Dict[str, Any] = dict()
    # TODO - Add metadata
    output.update(frontiers)
    write_json(args.frontier, output)


def get_ratings(
    scores_csv: str, fieldnames: List[str], fieldtypes: List[Callable]
) -> pd.DataFrame:
    """Convert ratings in a scores CSV file into a numpy array.

    TODO - Replace with scores_to_df
    """

    scores: List[Dict[str, str]] = list()
    with open(scores_csv, "r", encoding="utf-8-sig") as f:
        reader: DictReader[str] = DictReader(
            f, fieldnames=None, restkey=None, restval=None, dialect="excel"
        )
        for row in reader:
            scores.append(row)

    data: List[List[int]] = list()
    for score in scores:
        data.append([fieldtypes[i](score[f]) for i, f in enumerate(fieldnames)])

    df: pd.DataFrame = pd.DataFrame(data, columns=fieldnames)

    return df


def is_pareto_efficient_dumb(costs) -> np.ndarray:
    """
    Source: https://stackoverflow.com/questions/32791911/fast-calculation-of-pareto-front-in-python

    Very slow for many datapoints.  Fastest for many costs, most readable

    Find the pareto-efficient points
    :param costs: An (n_points, n_costs) array
    :return: A (n_points, ) boolean array, indicating whether each point is Pareto efficient
    """

    is_efficient: np.ndarray = np.ones(costs.shape[0], dtype=bool)
    for i, c in enumerate(costs):
        is_efficient[i] = np.all(np.any(costs[:i] > c, axis=1)) and np.all(
            np.any(costs[i + 1 :] > c, axis=1)
        )
    return is_efficient


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
        "frontier": "output/test_frontier.json",
    }
    args = require_args(args, args.debug, debug_defaults)

    return args


if __name__ == "__main__":
    main()

### END ###
