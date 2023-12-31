#!/usr/bin/env python3

"""
MAKE A BOX PLOT FOR RATINGS

For example:

$ scripts/make_box_plot.py \
--scores ~/iCloud/fileout/ensembles/NC20C_RMfRST_1000_scores.csv \
--no-debug

For documentation, type:

$ scripts/make_box_plot.py

TODO

- Background color
- Sample points
- Save to a file

"""

import argparse
from argparse import ArgumentParser, Namespace
from typing import Any, List, Dict, Callable

import plotly.express as px
import plotly.graph_objects as go

from rdabase import require_args

from tradeoffs import scores_to_df


def main() -> None:
    """Make a box plot of the ratings for the plans in an ensemble."""

    args: argparse.Namespace = parse_args()

    # Transform the ratings from a score CSV into a Pandas DataFrame

    fieldnames: List[str] = [
        "map",
        "proportionality",
        "competitiveness",
        "minority",
        "compactness",
        "splitting",
    ]
    fieldtypes: List[Callable] = [str, int, int, int, int, int]

    df = scores_to_df(args.scores, fieldnames, fieldtypes)

    # Configure & show the box plot for the ratings

    boxplot_traces: List[Dict] = []

    for name in fieldnames[1:]:
        trace: Dict = {
            "type": "box",
            "y": df[name],
            "name": name.capitalize(),
            "boxpoints": "all",  # Show individual points
            "jitter": 0.5,
            "whiskerwidth": 0.2,
            "marker": {"size": 2, "symbol": "circle"},
            "line": {"width": 1},
            "selectedpoints": [0],  # Highlight the first map
            "selected": {"marker": {"size": 5, "color": "black"}},
        }
        boxplot_traces.append(trace)

    boxplot_layout = {
        "width": 840,
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
        "paper_bgcolor": "#fafafa",
        "plot_bgcolor": "#fafafa",
    }

    boxplot_config = {
        "toImageButtonOptions": {
            "format": "png",  # one of png, svg, jpeg, webp
            "filename": "box-plot",
        },
        "modeBarButtonsToRemove": [
            "autoScale2d",
            "autoscale",
            "editInChartStudio",
            "editinchartstudio",
            "hoverCompareCartesian",
            "hovercompare",
            "lasso",
            "lasso2d",
            "orbitRotation",
            "orbitrotation",
            "pan",
            "pan2d",
            "pan3d",
            "reset",
            "resetCameraDefault3d",
            "resetCameraLastSave3d",
            "resetGeo",
            "resetSankeyGroup",
            "resetScale2d",
            "resetViewMapbox",
            "resetViews",
            "resetcameradefault",
            "resetcameralastsave",
            "resetsankeygroup",
            "resetscale",
            "resetview",
            "resetviews",
            "select",
            "select2d",
            "sendDataToCloud",
            "senddatatocloud",
            "tableRotation",
            "tablerotation",
            # "toImage", # Keep download button
            "toggleHover",
            "toggleSpikelines",
            "togglehover",
            "togglespikelines",
            "zoom",
            "zoom2d",
            "zoom3d",
            "zoomIn2d",
            "zoomInGeo",
            "zoomInMapbox",
            "zoomOut2d",
            "zoomOutGeo",
            "zoomOutMapbox",
            "zoomin",
            "zoomout",
        ],
        "displayModeBar": True,
        "displaylogo": False,
        "responsive": True,
    }

    fig = go.Figure()
    for t in boxplot_traces:
        fig.add_trace(go.Box(t))

    fig.update_layout(boxplot_layout)

    fig.show(config=boxplot_config)

    pass


def parse_args():
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Generate a collection of random maps."
    )

    parser.add_argument(
        "--scores",
        type=str,
        help="A CSV ensemble of scores including ratings to plot",
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
        "scores": "testdata/synthetic_ratings.csv"  # Only has map name & ratings,
    }
    args = require_args(args, args.debug, debug_defaults)

    return args


if __name__ == "__main__":
    main()

### END ###
