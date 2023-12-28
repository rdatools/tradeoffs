#!/usr/bin/env python3

"""
MAKE A BOX PLOT FOR SCORES

$ scripts/make_box_plot.py

"""

from typing import List, Dict, Callable

import plotly.express as px

# from plotly.subplots import make_subplots
# import plotly.graph_objects as go
# import chart_studio.plotly as py
# import plotly.graph_objs as go  # https://plotly.com/python-api-reference/plotly.graph_objects.html

from tradeoffs import scores_to_df

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

# labels: List[str] = [x.capitalize() for x in fieldnames[1:]]
fig = px.box(df, y=fieldnames[1:])  # , points="all")
fig.show()

pass

### END ###
