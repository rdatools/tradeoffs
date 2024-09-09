#!/usr/bin/env python3

"""
MAKE A BOX PLOT FOR RATINGS

For example, see the workflows directory.

For documentation, type:

$ scripts/make_box_plot.py -h

"""

import argparse
from argparse import ArgumentParser, Namespace
from typing import Any, List, Dict, Callable

import warnings

warnings.warn = lambda *args, **kwargs: None

import pandas as pd

import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

from rdabase import require_args
from rdaensemble.general import ratings_dimensions

from tradeoffs import scores_to_df, bgcolor, plot_width, plot_height, buttons


def main() -> None:
    """Make a box plot of the ratings for the plans in an ensemble."""

    args: argparse.Namespace = parse_args()
    filter: bool = not args.nofilter

    # Transform the ratings from a score CSV into a Pandas DataFrame

    fieldnames: List[str] = ["map"] + ratings_dimensions
    fieldtypes: List[Callable] = [str, int, int, int, int, int]

    df: pd.DataFrame = scores_to_df(
        args.scores,
        fieldnames,
        fieldtypes,
        roughly_equal=args.roughlyequal,
        filter=filter,
    )

    # Configure & show the box plot for the ratings

    boxplot_traces: List[Dict] = []

    for name in fieldnames[1:]:
        trace: Dict = {
            "type": "box",
            "y": df[name],
            "name": name.capitalize(),
            "boxpoints": "all",  # "outliers",
            "jitter": 0.5,
            "whiskerwidth": 0.2,
            "marker": {"size": 2, "symbol": "circle"},
            "line": {"width": 1},
            # "selectedpoints": focus_map,  # Highlight the first map
            # "selected": {"marker": {"size": 5, "color": "red"}},
        }
        boxplot_traces.append(trace)

    boxplot_layout = {
        "width": plot_width,
        "height": plot_height,
        "yaxis": {
            "showgrid": True,
            "zeroline": True,
            "tickvals": [i for i in range(0, 101, 5)],
            "gridcolor": "rgb(255, 255, 255)",
            "gridwidth": 1,
            "zerolinecolor": "rgb(255, 255, 255)",
            "zerolinewidth": 2,
        },
        "margin": {"l": 40, "r": 30, "b": 80, "t": 100},
        "showlegend": False,
        "paper_bgcolor": bgcolor,
        "plot_bgcolor": bgcolor,
    }

    boxplot_config = {
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
    for t in boxplot_traces:
        fig.add_trace(go.Box(t))

    fig.update_layout(boxplot_layout)

    if args.debug:  # Show the plot in a browser window
        fig.show(config=boxplot_config)
    else:  # Save the plot to a PNG file
        pio.kaleido.scope.default_format = "svg"
        pio.kaleido.scope.default_width = plot_width
        # pio.kaleido.scope.default_height
        pio.kaleido.scope.default_scale = 1

        fig.to_image(engine="kaleido")
        fig.write_image(args.image)

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
        "--roughlyequal",
        type=float,
        default=0.01,
        help="'Roughly equal' population threshold",
    )
    parser.add_argument(
        "--nofilter", dest="nofilter", action="store_true", help="Don't filter plans"
    )
    parser.add_argument(
        "--focus",
        nargs="?",
        type=str,
        default="",
        help="The flattened scores for a map to highlight (optional)",
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
        "scores": "testdata/test_scores.csv",  # Only has map name & ratings
        "image": "output/test_boxplot.svg",
    }
    args = require_args(args, args.debug, debug_defaults)

    return args


if __name__ == "__main__":
    main()

### END ###
