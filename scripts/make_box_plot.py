#!/usr/bin/env python3

"""
MAKE A BOX PLOT FOR SCORES

$ scripts/make_box_plot.py

"""

from typing import List, Dict, Callable

import plotly.express as px
import plotly.graph_objects as go

from tradeoffs import scores_to_df

# Transform scores into a Pandas DataFrame

scores_csv: str = "sample/sample_scores.csv"

fieldnames: List[str] = [
    "map",
    "proportionality",
    "competitiveness",
    "minority",
    "compactness",
    "splitting",
]
fieldtypes: List[Callable] = [str, int, int, int, int, int]

df = scores_to_df(scores_csv, fieldnames, fieldtypes)

# Configure & show the box plot - https://plotly.com/python/reference/box/

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

fig = go.Figure()
for t in boxplot_traces:
    fig.add_trace(go.Box(t))

fig.show()

pass

### END ###
