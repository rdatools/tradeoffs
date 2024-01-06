#!/usr/bin/env python3

"""
MAKE A SCATTER & LINE PLOT OF ENSEMBLE RATINGS AND FRONTIER

For example:

$ scripts/make_frontier_plot.py \
--scores testdata/synthetic_ratings.csv \
--frontier output/test_frontier.json \
--output ~/Downloads \
--no-debug

For documentation, type:

$ scripts/make_frontier_plot.py

TODO
"""

import argparse
from argparse import ArgumentParser, Namespace
from typing import Any, List, Dict, Callable

import pandas as pd
import itertools

import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

from rdabase import require_args, read_json
from rdaensemble.general import ratings_dimensions

from tradeoffs import scores_to_df, bgcolor, plot_width, plot_height, buttons


def main() -> None:
    """Make a box plot of the ratings for the plans in an ensemble."""

    args: argparse.Namespace = parse_args()

    # Transform the ratings from a score CSV into a Pandas DataFrame

    fieldnames: List[str] = ["map"] + ratings_dimensions
    fieldtypes: List[Callable] = [str, int, int, int, int, int]

    df: pd.DataFrame = scores_to_df(args.scores, fieldnames, fieldtypes)

    # Read the frontier from a JSON file

    data: Dict[str, Any] = read_json(args.frontier)
    frontiers: Dict[str, Any] = data["frontiers"]

    # For each pair of ratings dimensions, make a scatter plot of the ratings

    pairs: List = list(itertools.combinations(ratings_dimensions, 2))

    for p in pairs:
        d1: int = ratings_dimensions.index(p[0])
        d2: int = ratings_dimensions.index(p[1])
        ydim: str = ratings_dimensions[d1]
        xdim: str = ratings_dimensions[d2]

        pair: str = f"{ydim}_{xdim}"
        frontier: List[Dict] = frontiers[pair]

        # Configure & show the scatter plot for the ratings & frontier

        scatter_traces: List[Dict] = list()

        yvalues: List[int] = df[ydim].tolist()
        xvalues: List[int] = df[xdim].tolist()
        points_trace: Dict[str, Any] = {
            "x": xvalues,
            "y": yvalues,
            "mode": "markers",
            "marker_color": "gray",
            "marker_size": 2,
        }
        scatter_traces.append(points_trace)

        fyvalues: List[int] = [f["ratings"][d1] for f in frontier]
        fxvalues: List[int] = [f["ratings"][d2] for f in frontier]
        frontier_trace: Dict[str, Any] = {
            "x": fxvalues,
            "y": fyvalues,
            "mode": "lines+markers",
            "marker_color": "black",
            "marker_size": 5,
        }
        scatter_traces.append(frontier_trace)

        xlabel: str = xdim.capitalize()
        ylabel: str = ydim.capitalize()
        scatter_layout = {
            "width": plot_width,
            "height": plot_height,
            "yaxis": {
                "title_text": ylabel,
                "range": [0, 100],
                "showgrid": True,
                "zeroline": True,
                "dtick": 5,
                "gridcolor": "rgb(255, 255, 255)",
                "gridwidth": 1,
                "zerolinecolor": "rgb(255, 255, 255)",
                "zerolinewidth": 2,
            },
            "xaxis": {
                "title_text": xlabel,
                "range": [0, 100],
                "showgrid": True,
                "zeroline": True,
                "dtick": 5,
                "gridcolor": "rgb(255, 255, 255)",
                "gridwidth": 1,
                "zerolinecolor": "rgb(255, 255, 255)",
                "zerolinewidth": 2,
            },
            # "margin": {"l": 40, "r": 30, "b": 80, "t": 100},
            "showlegend": False,
            "paper_bgcolor": bgcolor,
            "plot_bgcolor": bgcolor,
        }
        scatter_config = {
            "toImageButtonOptions": {
                "format": "png",  # one of png, svg, jpeg, webp
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

        # fig.show(config=scatter_config)

        # TODO
        # if args.debug:  # Show the plot in a browser window
        #     fig.show(config=scatter_config)
        # else:  # Save the plot to a PNG file
        #     pio.kaleido.scope.default_format = "png"
        #     pio.kaleido.scope.default_width = plot_width
        #     # pio.kaleido.scope.default_height
        #     pio.kaleido.scope.default_scale = 1

        #     fig.to_image(engine="kaleido")
        #     fig.write_image(args.image)

        break  # TODO

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
        "--frontier",
        type=str,
        help="Frontier maps JSON file",
    )
    # parser.add_argument(
    #     "--image",
    #     type=str,
    #     help="The PNG file to download the box plot to",
    # )
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
        "scores": "testdata/synthetic_ratings.csv",  # Only has map name & ratings
        "frontier": "output/test_frontier.json",
        # "image": "output/test_boxplot.png",
        "output": "~/Downloads/",
    }
    args = require_args(args, args.debug, debug_defaults)

    return args


if __name__ == "__main__":
    main()

### END ###
