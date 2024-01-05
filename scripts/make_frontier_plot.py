#!/usr/bin/env python3

"""
MAKE A SCATTER & LINE PLOT OF ENSEMBLE RATINGS AND FRONTIER

For example:

$ scripts/make_frontier_plot.py \
--scores testdata/synthetic_ratings.csv \
--image output/test_boxplot.png \
--no-debug

For documentation, type:

$ scripts/make_frontier_plot.py

TODO
"""

import argparse
from argparse import ArgumentParser, Namespace
from typing import Any, List, Dict, Callable

import pandas as pd

import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

from rdabase import require_args
from tradeoffs import scores_to_df


def main() -> None:
    """Make a box plot of the ratings for the plans in an ensemble."""

    args: argparse.Namespace = parse_args()

    fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
    fig.show()

    pass


def parse_args():
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Make a box plot of the ratings for the plans in an ensemble."
    )

    parser.add_argument(
        "--scores",
        type=str,
        help="A CSV ensemble of scores including ratings to plot",
    )
    parser.add_argument(
        "--image",
        type=str,
        help="The PNG file to download the box plot to",
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
        "image": "output/test_boxplot.png",
    }
    args = require_args(args, args.debug, debug_defaults)

    return args


if __name__ == "__main__":
    main()

### END ###
