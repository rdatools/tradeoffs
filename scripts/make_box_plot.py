#!/usr/bin/env python3

"""
MAKE A BOX PLOT FOR SCORES

$ scripts/make_box_plot.py

"""

from typing import List, Dict

from csv import DictReader
import pandas as pd

import plotly.express as px

# import chart_studio.plotly as py
# import plotly.graph_objs as go  # https://plotly.com/python-api-reference/plotly.graph_objects.html

scores_csv: str = "sample/sample_scores.csv"


def read_scores(input: str) -> List[Dict[str, str]]:
    """Read a scores CSV file without fixed columns and return a list of dictionaries."""

    scores: List[Dict[str, str]] = list()

    with open(input, "r", encoding="utf-8-sig") as f:
        reader: DictReader[str] = DictReader(
            f, fieldnames=None, restkey=None, restval=None, dialect="excel"
        )
        fieldnames: List[str] = list(reader.fieldnames) if reader.fieldnames else []
        for row in reader:
            # row_out: Dict = dict(zip(fieldnames, row))
            scores.append(row)

    return scores


scores: List[Dict[str, str]] = read_scores(scores_csv)

xdata: List[str] = [
    "Proportionality",
    "Competitiveness",
    "Minority",
    "Compactness",
    "Splitting",
]
ydata: List[List[int]] = list()
for score in scores:
    ydata.append([int(score[d.lower()]) for d in xdata])

df = pd.DataFrame(ydata, columns=xdata)

# print(df)

pass

df = px.data.tips()
fig = px.box(df, x="time", y="total_bill", points="all")
fig.show()

pass

"""
https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html
https://plotly.com/python/static-image-export/

https://dash.plotly.com/installation
https://plotly.com/python/box-plots/

"""
