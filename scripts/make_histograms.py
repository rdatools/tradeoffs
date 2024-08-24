#!/usr/bin/env python3

"""
MAKE HISTORGRAMS

For example:

$ scripts/make_histograms.py \
--scores ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_scores.csv \
--prefix NC20C \
--output ../../iCloud/fileout/tradeoffs/NC/assets/images/ \
--no-debug

For documentation, type:

$ scripts/make_histograms.py -h
"""

import argparse
from argparse import ArgumentParser, Namespace

from typing import List, Dict, Any, Callable

import warnings

warnings.warn = lambda *args, **kwargs: None

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.io as pio

from rdabase import require_args, read_json
from rdaensemble.general import ratings_dimensions

from tradeoffs import scores_to_df


def main() -> None:
    """Make historgrams for the ratings for the plans in an ensemble."""

    args: argparse.Namespace = parse_args()

    fieldnames: List[str] = ["map"] + ratings_dimensions
    fieldtypes: List[Callable] = [str, int, int, int, int, int]

    df: pd.DataFrame = scores_to_df(args.scores, fieldnames, fieldtypes)

    for dimension in ratings_dimensions:
        counts, bins = np.histogram(df[dimension], bins=range(0, 100, 5))
        bins = 0.5 * (bins[:-1] + bins[1:])

        fig = px.bar(x=bins, y=counts, labels={"x": dimension, "y": "count"})
        # fig = px.histogram(df, x=dimension, nbins=20)

        if args.debug:  # Show the plot in a browser window
            fig.show()
            continue
        else:  # Save the plot to a PNG file
            plot_path: str = f"{args.output}/{args.prefix}_{dimension}_histogram.png"
            pio.kaleido.scope.default_format = "png"
            fig.to_image(engine="kaleido")
            fig.write_image(plot_path)

        pass


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
        "--prefix",
        type=str,
        help="The plot filename prefix",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="~/Downloads/",
        help="Path to output directory",
        type=str,
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
        "prefix": "NC20C",
        "output": "~/Downloads/",
    }
    args = require_args(args, args.debug, debug_defaults)

    return args


if __name__ == "__main__":
    main()

### END ###
