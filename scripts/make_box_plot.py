#!/usr/bin/env python3

"""
MAKE A BOX PLOT FOR RATINGS

For example:

$ scripts/make_box_plot.py \
--scores ../../iCloud/fileout/ensembles/NC20C_ReCom_1K_scores.csv \
--image ../../iCloud/fileout/images/NC20C_boxplot.png \
--no-debug

$ scripts/make_box_plot.py \
--scores ../../iCloud/fileout/ensembles/NC20C_ReCom_1K_scores.csv \
--focus ../../iCloud/fileout/ensembles/NC_2024_Congressional_scores.csv \
--image ../../iCloud/fileout/images/NC20C_boxplot.png \
--no-debug

For documentation, type:

$ scripts/make_box_plot.py

"""

import argparse
from argparse import ArgumentParser, Namespace
from typing import Any, List, Dict, Callable

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

    # Transform the ratings from a score CSV into a Pandas DataFrame

    fieldnames: List[str] = ["map"] + ratings_dimensions
    fieldtypes: List[Callable] = [str, int, int, int, int, int]

    df: pd.DataFrame = scores_to_df(args.scores, fieldnames, fieldtypes)

    # If given, read ratings for a "focus map" from a CSV file
    focus_map: List[int] = []
    if args.focus:
        focus_df: pd.DataFrame = scores_to_df(args.focus, fieldnames, fieldtypes)
        # TODO - Nudge 0 & 100 ratings up and down 1 to show better in the plot?
        df = pd.concat([focus_df, df])
        focus_map = [0]

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
            "selectedpoints": focus_map,  # Highlight the first map
            "selected": {"marker": {"size": 5, "color": "red"}},
        }
        boxplot_traces.append(trace)

    boxplot_layout = {
        "width": plot_width,
        "height": plot_height,
        "yaxis": {
            "range": [0, 100],
            "showgrid": True,
            "zeroline": True,
            "dtick": 5,
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
            "format": "png",  # one of png, svg, jpeg, webp
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
        pio.kaleido.scope.default_format = "png"
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
        "scores": "testdata/synthetic_ratings.csv",  # Only has map name & ratings
        "focus": "testdata/map_scores.csv",
        "image": "output/test_boxplot.png",
    }
    args = require_args(args, args.debug, debug_defaults)

    return args


if __name__ == "__main__":
    main()

### END ###
