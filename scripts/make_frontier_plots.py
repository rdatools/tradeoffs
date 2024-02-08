#!/usr/bin/env python3

"""
MAKE A SCATTER & LINE PLOT OF ENSEMBLE RATINGS AND FRONTIER

For example:

$ scripts/make_frontier_plots.py \
--scores ../../iCloud/fileout/ensembles/NC20C_ReCom_1K_scores.csv \
--frontier ../../iCloud/fileout/ensembles/NC20C_ReCom_1K_frontiers.json \
--prefix NC20C \
--output ../../iCloud/fileout/images/ \
--no-debug

$ scripts/make_frontier_plots.py \
--scores ../../iCloud/fileout/ensembles/NC20C_ReCom_1K_scores.csv \
--frontier ../../iCloud/fileout/ensembles/NC20C_ReCom_1K_frontiers.json \
--focus ../../iCloud/fileout/ensembles/NC_2024_Congressional_scores.csv \
--prefix NC20C \
--output ../../iCloud/fileout/images/ \
--no-debug

For documentation, type:

$ scripts/make_frontier_plots.py

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

    # TODO
    # Read the focus map from a CSV file
    focus_ratings: List[int] = []
    if args.focus:
        focus_df: pd.DataFrame = scores_to_df(args.focus, fieldnames, fieldtypes)
        focus_ratings = focus_df.iloc[0][ratings_dimensions].to_list()

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

        scatter_traces: List[Dict] = []

        yvalues: List[int] = df[ydim].tolist()
        xvalues: List[int] = df[xdim].tolist()
        points_trace: Dict[str, Any] = {
            "x": xvalues,
            "y": yvalues,
            "mode": "markers",
            "marker_color": "black",
            "marker_size": 1,
        }
        scatter_traces.append(points_trace)

        # TODO
        if args.focus:
            focus_trace: Dict[str, Any] = {
                "x": [focus_ratings[d2]],
                "y": [focus_ratings[d1]],
                "mode": "markers",
                "marker_symbol": "star",
                "marker_color": "red",
                "marker_size": 9,
            }
            scatter_traces.append(focus_trace)

        fyvalues: List[int] = [f["ratings"][d1] for f in frontier]
        fxvalues: List[int] = [f["ratings"][d2] for f in frontier]
        frontier_trace: Dict[str, Any] = {
            "x": fxvalues,
            "y": fyvalues,
            "mode": "markers",
            "marker_color": "black",
            "marker_size": 5,
        }
        scatter_traces.append(frontier_trace)

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

        if False and args.debug:  # Show the plot in a browser window
            fig.show(config=scatter_config)
            continue
        else:  # Save the plot to a PNG file
            pio.kaleido.scope.default_format = "png"
            pio.kaleido.scope.default_width = plot_width
            # pio.kaleido.scope.default_height
            pio.kaleido.scope.default_scale = 1

            plot_path: str = f"{args.output}/{args.prefix}_{pair}_scatter.png"

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
        help="A CSV ensemble of scores including ratings to plot",
    )
    parser.add_argument(
        "--frontier",
        type=str,
        help="Frontier maps JSON file",
    )
    parser.add_argument(
        "--focus",
        nargs="?",
        type=str,
        default="",
        help="The flattened scores for a map to highlight (optional)",
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
        "scores": "testdata/synthetic_ratings.csv",  # Only has map name & ratings
        "frontier": "output/test_frontiers.json",
        "focus": "testdata/map_scores.csv",
        "prefix": "test",
        "output": "output",
    }
    args = require_args(args, args.debug, debug_defaults)

    return args


if __name__ == "__main__":
    main()

### END ###
