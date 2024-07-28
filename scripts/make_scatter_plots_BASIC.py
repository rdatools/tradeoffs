#!/usr/bin/env python3

"""
MAKE SCATTER PLOTS OF ENSEMBLE RATINGS FOR PAIRS OF RATINGS ALONG WITH FRONTIERS
- A basic version for testing new opportunity-district-only minority ratings

For example, see the workflows directory.

For documentation, type:

$ scripts/make_scatter_plots_BASIC.py -h

"""

import argparse
from argparse import ArgumentParser, Namespace
from typing import Any, List, Dict, Tuple, Callable

import warnings

warnings.warn = lambda *args, **kwargs: None

import pandas as pd
import itertools
import numpy as np

import plotly.graph_objects as go
import plotly.io as pio

from rdabase import require_args, read_json, read_csv, write_csv
from rdaensemble.general import ratings_dimensions

from tradeoffs import (
    scores_to_df,
    bgcolor,
    plot_width,
    plot_height,
    buttons,
    line_segment_hull,
)


def main() -> None:
    """Make a box plot of the ratings for the plans in an ensemble."""

    args: argparse.Namespace = parse_args()

    # Transform the ratings from a score CSV into a Pandas DataFrame

    fieldnames: List[str] = ["map"] + ratings_dimensions
    fieldtypes: List[Callable] = [str, int, int, int, int, int]

    df: pd.DataFrame = scores_to_df(args.scores, fieldnames, fieldtypes)

    pairs: List = list(itertools.combinations(ratings_dimensions, 2))

    # If given, read the focus map ratings & convert them to scatter plot points

    legend: List[Dict[str, str]] = []

    # Read the notable map ratings & convert them to scatter plot points

    map_to_dimension: Dict[str, str] = {
        "Official": "official",
        "Most Proportional": "proportionality",
        "Most Competitive": "competitiveness",
        "Best Minority": "minority",
        "Most Compact": "compactness",
        "Least Splitting": "splitting",
    }

    # For each pair of ratings dimensions, make a scatter plot of the ratings

    for p in pairs:
        ydim: str = p[0]
        xdim: str = p[1]
        d1: int = ratings_dimensions.index(ydim)
        d2: int = ratings_dimensions.index(xdim)

        pair: str = f"{ydim}_{xdim}"

        # Configure & show the scatter plot for the ratings & frontier

        yvalues: List[int] = df[ydim].tolist()
        xvalues: List[int] = df[xdim].tolist()
        points_trace: Dict[str, Any] = {
            "x": xvalues,
            "y": yvalues,
            "mode": "markers",
            "marker_color": "black",
            "marker_size": 1,
            "showlegend": False,
        }

        # Add the traces in the desired order

        scatter_traces: List[Dict] = []
        scatter_traces.append(points_trace)

        # Configure & show the scatter plot for the ratings & frontier

        xlabel: str = xdim.capitalize()
        ylabel: str = ydim.capitalize()
        xy_range: List[int] = [-1, 101]
        height: int = 500
        width: int = round(height * 0.80)
        scatter_layout = {
            "autosize": False,
            "width": width,
            "height": height,
            "yaxis": {
                "title_text": ylabel,
                "range": xy_range,
                "showgrid": True,
                "zeroline": True,
                "tickvals": [i for i in range(0, 101, 5)],
                "gridcolor": "lightgray",
                "gridwidth": 1,
                "zerolinecolor": "rgb(255, 255, 255)",
                "zerolinewidth": 2,
            },
            "xaxis": {
                "title_text": xlabel,
                "range": xy_range,
                "showgrid": True,
                "zeroline": True,
                "tickvals": [i for i in range(0, 101, 5)],
                "gridcolor": "lightgray",
                "gridwidth": 1,
                "zerolinecolor": "rgb(255, 255, 255)",
                "zerolinewidth": 2,
                "scaleanchor": "y",
                "scaleratio": 1,
            },
            "margin": {"l": 40, "r": 30, "b": 80, "t": 100},
            # "legend": {"yanchor": "top", "y": 0.99, "xanchor": "left", "x": 0.01},
            "showlegend": False,
            # "showlegend": False,
            "paper_bgcolor": bgcolor,
            "plot_bgcolor": bgcolor,
        }
        scatter_config = {
            "toImageButtonOptions": {
                "format": "svg",  # one of png, svg, jpeg, webp
                "filename": "box-plot",
            },
            "modeBarButtonsToRemove": buttons,
            "displayModeBar": True,
            "displaylogo": False,
            "responsive": True,
        }

        fig = go.Figure()
        for t in scatter_traces:
            fig.add_trace(go.Scatter(t))

        fig.update_layout(scatter_layout)

        if False and args.debug:  # Show the plot in a browser window
            fig.show(config=scatter_config)
            continue
        else:  # Save the plot to an SVG file
            pio.kaleido.scope.default_format = "svg"

            pio.kaleido.scope.default_width = plot_width
            # pio.kaleido.scope.default_height
            pio.kaleido.scope.default_scale = 1

            suffix: str = "" if len(args.suffix) == 0 else f"_{args.suffix}"

            plot_path: str = f"{args.output}/{args.prefix}_{pair}{suffix}_scatter.svg"

            fig.to_image(engine="kaleido")
            fig.write_image(plot_path)

        continue


def parse_args():
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Make a box plot of the ratings for the plans in an ensemble."
    )

    parser.add_argument(
        "--scores",
        type=str,
        help="A CSV of scores including ratings to plot",
    )
    parser.add_argument(
        "--prefix",
        type=str,
        help="The plot filename prefix",
    )
    parser.add_argument(
        "--suffix",
        type=str,
        default="",
        help="The plot filename suffix",
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
        "scores": "../../iCloud/fileout/tradeoffs/SC/ensembles/SC20C_scores.csv",
        "prefix": "SC20C",
        "suffix": "",
        "output": "~/Downloads/",
        "verbose": True,
    }
    args = require_args(args, args.debug, debug_defaults)

    return args


if __name__ == "__main__":
    main()

### END ###
