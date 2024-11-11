#!/usr/bin/env python3

"""
PLOT PAIRS OF METRICS for quick sanity checks

For example:

$ scripts-1time/plot_pairs.py --scores ../../temp/tradeoffs/NC/ensembles/NC20C_scores.csv --no-debug

$ scripts-1time/plot_pairs.py \
--scores ../../temp/tradeoffs/NC/ensembles/NC20C_scores.csv \
--more ../../temp/tradeoffs/NC/ensembles/multiple-starts/NC20C_scores_RANDOM.csv \
--no-debug

$ scripts-1time/plot_pairs.py \
--scores ../../temp/tradeoffs/NC/ensembles/spanning-tree/NC20C_scores_WILSON.csv \
--more ../../temp/tradeoffs/NC/ensembles/multiple-starts/NC20C_scores_RANDOM.csv \
--no-debug

For documentation, type:

$ scripts-1time/plot_pairs.py -h
"""

import argparse
from argparse import ArgumentParser, Namespace

from typing import Any, List, Dict, Callable, Optional

import itertools
import matplotlib.pyplot as plt
import pandas as pd

from rdabase import require_args
from tradeoffs.readwrite import scores_to_df


def main() -> None:
    """Make pairwise plots of metrics in a score CSV."""

    args: argparse.Namespace = parse_args()

    #

    x_inputs: List[str] = [
        "D",
        "C",
        "efficiency_gap",
        "average_margin",
        "proportional_opportunities",
        "alt_opportunity_districts",
        "defined_opportunity_districts",
        "polsby_popper",
        "county_splitting",
        "counties_split",
        "county_splits",
    ]
    x_inputs_types: List[type] = [
        int,
        int,
        float,
        float,
        int,
        float,
        int,
        float,
        float,
        int,
        int,
    ]
    x_metrics: List[str] = [
        "efficiency_gap",
        "average_margin",
        "defined_opportunity_pct",
        "polsby_popper",
        "county_splitting",
    ]

    # Read the scores from a CSV file into a Pandas dataframe

    fieldnames: List[str] = x_inputs
    fieldtypes: List[Callable] = x_inputs_types

    scores: pd.DataFrame = scores_to_df(
        args.scores,
        fieldnames,
        fieldtypes,
    )

    more: Optional[pd.DataFrame] = (
        scores_to_df(
            args.more,
            fieldnames,
            fieldtypes,
        )
        if args.more
        else None
    )

    # Compute derived metrics

    for df in [scores, more]:
        if df is not None:
            df["defined_opportunity_pct"] = (
                df["defined_opportunity_districts"] / df["proportional_opportunities"]
            )
            df["county_splits_ratio"] = df["county_splits"] / df["D"]

    # Plot each pair of metrics

    pairs: List = list(itertools.combinations(x_metrics, 2))

    for pair in pairs:
        y_metric: str = pair[0]
        x_metric: str = pair[1]

        plt.figure(figsize=(10, 6))

        # y = scores[y_metric]
        # x = scores[x_metric]

        # plt.scatter(x, y, color="blue", alpha=0.6)

        plt.scatter(
            scores[x_metric],
            scores[y_metric],
            color="blue",
            alpha=0.6,
            label="Ensemble points",
        )
        if more is not None:
            plt.scatter(
                more[x_metric],
                more[y_metric],
                color="red",
                alpha=0.6,
                label="Extra points",
            )

        plt.xlabel(x_metric)
        plt.ylabel(y_metric)

        plt.grid(True, linestyle="--", alpha=0.7)
        plt.legend()

        plt.show()

        pass

    pass


def parse_args():
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Make pairwise plots of metrics in a score CSV."
    )

    parser.add_argument(
        "--scores",
        type=str,
        help="A CSV ensemble of scores including ratings to plot",
    )
    parser.add_argument(
        "--more",
        type=str,
        help="An optional second CSV ensemble of scores to plot",
    )

    # Enable debug/explicit mode
    parser.add_argument("--debug", default=True, action="store_true", help="Debug mode")
    parser.add_argument(
        "--no-debug", dest="debug", action="store_false", help="Explicit mode"
    )

    args: Namespace = parser.parse_args()

    # Default values for args in debug mode
    debug_defaults: Dict[str, Any] = {
        "scores": "../../temp/tradeoffs/NC/ensembles/NC20C_scores.csv",
        "more": "../../temp/tradeoffs/NC/ensembles/multiple-starts/NC20C_scores_RANDOM.csv",  # None,
    }
    args = require_args(args, args.debug, debug_defaults)

    return args


if __name__ == "__main__":
    main()

### END ###
