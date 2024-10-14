#!/usr/bin/env python3

"""
PLOT PAIRS OF METRICS for quick sanity checks
"""

from typing import List, Callable

import itertools
import matplotlib.pyplot as plt
import pandas as pd

from tradeoffs.readwrite import scores_to_df


# Setup

scores_csv = "../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_scores_100.csv"

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
    "county_splitting",
]

# Read the scores from a CSV file into a Pandas dataframe

fieldnames: List[str] = x_inputs
fieldtypes: List[Callable] = x_inputs_types

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

pairs: List = list(itertools.combinations(x_metrics, 2))

for pair in pairs:
    y_metric: str = pair[0]
    x_metric: str = pair[1]

    y = scores[y_metric]
    x = scores[x_metric]

    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, color="blue", alpha=0.6)

    plt.xlabel(x_metric)
    plt.ylabel(y_metric)

    plt.grid(True, linestyle="--", alpha=0.7)

    plt.show()

    pass

pass

### END ###
