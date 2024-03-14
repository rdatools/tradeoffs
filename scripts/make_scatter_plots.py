#!/usr/bin/env python3

"""
MAKE SCATTER PLOTS OF ENSEMBLE RATINGS FOR PAIRS OF RATINGS ALONG WITH FRONTIERS

For example:

$ scripts/make_scatter_plots.py \
--scores ../../iCloud/fileout/ensembles/NC20C_scores.csv \
--frontier ../../iCloud/fileout/ensembles/NC20C_frontiers.json \
--pushed ../../iCloud/fileout/ensembles/NC20C_frontiers_pushed.json \
--notables docs/_data/notable_ratings/NC_2022_Congress_ratings.csv \
--focus ../../iCloud/fileout/ensembles/NC20C_focus_scores.csv \
--prefix NC20C \
--output ../../iCloud/fileout/images \
--no-debug

scripts/make_scatter_plots.py \
--scores ../../iCloud/fileout/ensembles/NC20C_scores.csv \
--more ../../iCloud/fileout/ensembles/NC20C_scores_more.csv \
--frontier ../../iCloud/fileout/ensembles/NC20C_frontiers.json \
--pushed ../../iCloud/fileout/ensembles/NC20C_frontiers_pushed.json \
--notables docs/_data/notable_ratings/NC_2022_Congress_ratings.csv \
--focus ../../iCloud/fileout/ensembles/NC20C_focus_scores.csv \
--prefix NC20C \
--output ~/Downloads \
--no-debug

For documentation, type:

$ scripts/make_scatter_plots.py

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
    if args.more:
        more_df: pd.DataFrame = scores_to_df(args.more, fieldnames, fieldtypes)

    # Read the frontier from a JSON file

    data: Dict[str, Any] = read_json(args.frontier)
    frontiers: Dict[str, Any] = data["frontiers"]

    pairs: List = list(itertools.combinations(ratings_dimensions, 2))

    # If given, read the pushed frontier

    if args.pushed:
        data = read_json(args.pushed)
        pushed_frontiers: Dict[str, Any] = data["frontiers"]

    # If given, read the focus map ratings & convert them to scatter plot points

    legend: List[Dict[str, str]] = []
    if args.focus:
        ratings_table: List[Dict[str, str | int]] = read_csv(
            args.focus, [str, int, int, int, int, int]
        )
        focus_markers: List[str] = ["cross", "circle", "x", "square", "star"]

        if len(ratings_table) > len(focus_markers):
            raise Exception(
                f"More focus maps than focus markers ({len(focus_markers)})."
            )

        focus_ratings: Dict[str, List[int]] = {}
        for i, m in enumerate(ratings_table):
            name: str = str(m["Map"])
            ratings: List[int] = [int(v) for k, v in m.items() if k != "Map"]
            focus_ratings[name] = ratings
            legend.append({"MARKER": f"Black {focus_markers[i]}", "PLAN": f"{name}"})
        legend.append({"MARKER": f"Red diamonds", "PLAN": "DRA notable maps"})

        focus_names: List[str] = []
        focus_points: Dict[Tuple, List[Tuple[int, int]]] = {}
        for p in pairs:
            ydim: str = p[0]
            xdim: str = p[1]
            d1: int = ratings_dimensions.index(ydim)
            d2: int = ratings_dimensions.index(xdim)

            focus_points[p] = []
            for name, ratings in focus_ratings.items():
                focus_points[p].append(
                    (focus_ratings[name][d2], focus_ratings[name][d1])
                )
                focus_names.append(name)

    # Read the notable map ratings & convert them to scatter plot points

    ratings_table: List[Dict[str, str | int]] = read_csv(
        args.notables, [str, int, int, int, int, int]
    )
    map_to_dimension: Dict[str, str] = {
        "Official": "official",
        "Most Proportional": "proportionality",
        "Most Competitive": "competitiveness",
        "Best Minority": "minority",
        "Most Compact": "compactness",
        "Least Splitting": "splitting",
    }
    notable_ratings: Dict[str, List[int]] = {}
    for m in ratings_table:
        name: str = map_to_dimension[str(m["MAP"])]
        ratings: List[int] = [int(v) for k, v in m.items() if k != "MAP"]
        notable_ratings[name] = ratings

    notable_points: Dict[Tuple, List[Tuple[int, int]]] = {}
    official_points: Dict[Tuple, Tuple[int, int]] = {}
    for p in pairs:
        ydim: str = p[0]
        xdim: str = p[1]
        d1: int = ratings_dimensions.index(ydim)
        d2: int = ratings_dimensions.index(xdim)

        notable_points[p] = []
        notable_points[p].append((notable_ratings[ydim][d2], notable_ratings[ydim][d1]))
        notable_points[p].append((notable_ratings[xdim][d2], notable_ratings[xdim][d1]))

        official_points[p] = (
            notable_ratings["official"][d2],
            notable_ratings["official"][d1],
        )

    # For each pair of ratings dimensions, make a scatter plot of the ratings

    for p in pairs:
        ydim: str = p[0]
        xdim: str = p[1]
        d1: int = ratings_dimensions.index(ydim)
        d2: int = ratings_dimensions.index(xdim)

        pair: str = f"{ydim}_{xdim}"
        frontier: List[Dict] = frontiers[pair]
        pushed_frontier: List[Dict] = []
        if args.pushed:
            pushed_frontier = pushed_frontiers[pair]

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

        if args.more:
            myvalues: List[int] = more_df[ydim].tolist()
            mxvalues: List[int] = more_df[xdim].tolist()
            more_points_trace: Dict[str, Any] = {
                "x": mxvalues,
                "y": myvalues,
                "mode": "markers",
                "marker_color": "green",
                "marker_size": 1,
                "showlegend": False,
            }

        notable_traces: List[Dict[str, Any]] = []
        for pt in notable_points[p]:
            notable_trace: Dict[str, Any] = {
                "x": [pt[0]],
                "y": [pt[1]],
                "mode": "markers",
                "marker": {"size": 5, "color": "red", "symbol": "diamond"},
                "showlegend": False,
            }
            notable_traces.append(notable_trace)
        # official_trace: Dict[str, Any] = {
        #     "x": [official_points[p][0]],
        #     "y": [official_points[p][1]],
        #     "mode": "markers",
        #     "marker": {"size": 5, "symbol": "star"},
        # }

        focus_traces: List[Dict[str, Any]] = []
        if args.focus:
            for i, pt in enumerate(focus_points[p]):
                focus_trace: Dict[str, Any] = {
                    "name": focus_names[i],
                    "x": [pt[0]],
                    "y": [pt[1]],
                    "mode": "markers",
                    "marker": {"size": 5, "color": "black", "symbol": focus_markers[i]},
                    "showlegend": False,
                }
                focus_traces.append(focus_trace)

        fyvalues: List[int] = [f["ratings"][d1] for f in frontier]
        fxvalues: List[int] = [f["ratings"][d2] for f in frontier]
        frontier_trace: Dict[str, Any] = {
            "x": fxvalues,
            "y": fyvalues,
            "mode": "lines",
            "line_color": "lightgray",
            "fill": None,
            "showlegend": False,
        }

        if args.pushed:
            pfpts: List[Tuple[int, int]] = [
                (f["ratings"][d2], f["ratings"][d1]) for f in pushed_frontier
            ]
            pfpts = list(set(pfpts))  # Remove duplicates
            pfpts = sorted(
                pfpts, key=lambda pt: (pt[1], pt[0]), reverse=True
            )  # Re-sort the remaining points

            pfyvalues: List[int] = [pt[1] for pt in pfpts]
            pfxvalues: List[int] = [pt[0] for pt in pfpts]
            if args.verbose:
                print(
                    f"Pushed frontier ({ratings_dimensions[d1]}, {ratings_dimensions[d2]}) has {len(pfyvalues)} points."
                )
            pushed_frontier_trace: Dict[str, Any] = {
                "x": pfxvalues,
                "y": pfyvalues,
                "mode": "markers",
                "marker_color": "black",
                "marker_size": 2,
                "fill": None,
                "showlegend": False,
            }

            hyvalues: List[int]
            hxvalues: List[int]
            hxvalues, hyvalues = line_segment_hull(pfxvalues, pfyvalues)
            # hxvalues, hyvalues = pfxvalues, pfyvalues
            hull_trace: Dict[str, Any] = {
                "x": hxvalues,
                "y": hyvalues,
                "mode": "lines+markers",
                "line_color": "black",
                "marker_size": 3,
                "marker_color": "black",
                "fill": "tonexty",
                "fillcolor": "lightgray",
                "showlegend": False,
            }

        # Add the traces in the desired order

        scatter_traces: List[Dict] = []
        scatter_traces.append(points_trace)
        # scatter_traces.append(official_trace)
        scatter_traces.append(frontier_trace)
        if args.pushed:
            scatter_traces.append(hull_trace)
            scatter_traces.append(pushed_frontier_trace)
        if args.more:
            scatter_traces.append(more_points_trace)
        for notable_trace in notable_traces:
            scatter_traces.append(notable_trace)
        if args.focus:
            for focus_trace in focus_traces:
                scatter_traces.append(focus_trace)

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

            if args.focus:
                legend_path: str = f"{args.output}/{args.prefix}_legend.csv"
                write_csv(legend_path, legend, ["MARKER", "PLAN"])

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
        "--more",
        nargs="?",
        type=str,
        default="",
        help="Another CSV of scores including ratings to plot",
    )
    parser.add_argument(
        "--notables",
        type=str,
        help="A CSV file of notable maps ratings",
    )
    parser.add_argument(
        "--frontier",
        type=str,
        help="Frontier maps JSON file",
    )
    parser.add_argument(
        "--pushed",
        nargs="?",
        type=str,
        default="",
        help="Pushed frontier maps JSON file",
    )
    parser.add_argument(
        "--focus",
        nargs="?",
        type=str,
        default="",
        help="The ratings for maps to highlight (optional)",
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
        "scores": "../../iCloud/fileout/ensembles/NC20C_scores.csv",
        "more": "../../iCloud/fileout/ensembles/NC20C_scores_more.csv",
        "frontier": "../../iCloud/fileout/ensembles/NC20C_frontiers.json",
        "pushed": "../../iCloud/fileout/ensembles/NC20C_frontiers_pushed.json",
        "notables": "docs/_data/notable_ratings/NC_2022_Congress_ratings.csv",
        "focus": "../../iCloud/fileout/ensembles/NC20C_focus_scores.csv",
        "prefix": "NC20C",
        "suffix": "",
        "output": "~/Downloads/",
        "verbose": True,
    }
    args = require_args(args, args.debug, debug_defaults)

    return args


if __name__ == "__main__":
    main()

### END ###
