#!/usr/bin/env python3

"""
COMPARE DRA RATINGS (Y) to OTHER METRICS (X)
"""

from typing import List, Callable

import csv
import matplotlib.pyplot as plt
import pandas as pd

from tradeoffs.readwrite import scores_to_df


# Setup

scores_csv = "../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_scores_100.csv"

y_metrics: List[str] = [
    "proportionality",
    "competitiveness",
    "minority",
    "compactness",
    "splitting",
]
y_types: List[type] = [int] * 5

x_inputs: List[str] = [
    "D",
    "C",
    "efficiency_gap",
    "average_margin",
    "proportional_opportunities",
    "alt_opportunity_districts",
    "defined_opportunity_districts",
    "polsby_popper",
    "counties_split",
    "county_splits",
]
x_inputs_types: List[type] = [
    int,
    int,
    float,
    float,
    int,
    float,
    int,
    float,
    int,
    int,
]
x_metrics: List[str] = [
    "efficiency_gap",
    "average_margin",
    "defined_opportunity_pct",
    "polsby_popper",
    "county_splits_ratio",
]

# Read the scores from a CSV file into a Pandas dataframe

fieldnames: List[str] = y_metrics + x_inputs
fieldtypes: List[Callable] = y_types + x_inputs_types

scores: pd.DataFrame = scores_to_df(
    scores_csv,
    fieldnames,
    fieldtypes,
)

# Compute derived metrics

scores["defined_opportunity_pct"] = (
    scores["defined_opportunity_districts"] / scores["proportional_opportunities"]
)
scores["county_splits_ratio"] = scores["county_splits"] / scores["D"]

# Plot each pair of metrics

for y_metric, x_metric in zip(y_metrics, x_metrics):

    y = scores[y_metric]
    x = scores[x_metric]

    # Create the scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, color="blue", alpha=0.6)

    # Add labels and title
    plt.xlabel(x_metric)
    plt.ylabel(y_metric)
    # plt.title('2D Scatter Plot')

    # Add a grid
    plt.grid(True, linestyle="--", alpha=0.7)

    # Show the plot
    plt.show()

    pass

pass

### END ###
