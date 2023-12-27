#!/usr/bin/env python3

"""
MAKE A BOX PLOT FOR SCORES

$ scripts/make_box_plot.py

"""

from typing import List, Dict

from csv import DictReader
import pandas as pd

# from plotly.subplots import make_subplots
# import plotly.graph_objects as go

import plotly.express as px

# import chart_studio.plotly as py
# import plotly.graph_objs as go  # https://plotly.com/python-api-reference/plotly.graph_objects.html

scores_csv: str = "sample/sample_scores.csv"


def ratings_to_df(scores_csv: str, dimensions: List[str]) -> pd.DataFrame:
    """Convert ratings in a scores CSV file into a Pandas dataframe."""

    scores: List[Dict[str, str]] = list()
    with open(scores_csv, "r", encoding="utf-8-sig") as f:
        reader: DictReader[str] = DictReader(
            f, fieldnames=None, restkey=None, restval=None, dialect="excel"
        )
        fieldnames: List[str] = list(reader.fieldnames) if reader.fieldnames else []
        for row in reader:
            scores.append(row)

    ratings: List[List[int]] = list()
    for score in scores:
        ratings.append([int(score[d.lower()]) for d in dimensions])

    df: pd.DataFrame = pd.DataFrame(ratings, columns=dimensions)

    return df


columns: List[str] = [
    "Proportionality",
    "Competitiveness",
    "Minority",
    "Compactness",
    "Splitting",
]

df = ratings_to_df(scores_csv, columns)
fig = px.box(df, y=columns, points="all")
fig.show()

pass

"""
https://stackoverflow.com/questions/62901783/how-to-plot-boxplots-of-multiple-columns-with-different-ranges

fig = make_subplots(rows=1, cols=len(xdata))
for i, dim in enumerate(xdata):
    fig.add_trace(go.Box(y=df[dim], name=dim), row=1, col=i + 1)
fig.update_traces(boxpoints="all", jitter=0.3)

https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html
https://plotly.com/python/static-image-export/

https://dash.plotly.com/installation
https://plotly.com/python/box-plots/

"""
