#!/usr/bin/env python3

"""
MAKE AN X by Y SCATTER PLOT

(for comparing how two metrics relate to each other)

"""

from typing import List, Dict, Any

import csv
import matplotlib.pyplot as plt

# from rdabase import read_csv

csv_file = (
    "../../iCloud/fileout/tradeoffs/NC/analysis/NC20C_scores - EGxProportionality.csv"
)
x_label: str = "EG'"
y_label: str = "proportionality"
x_type: type = float
y_type: type = int

# metrics: List[Dict[str, Any]] = read_csv(csv_file, [float, int])
with open(csv_file, "r") as file:
    csv_reader = csv.DictReader(file)

    x: List[float] = []
    y: List[int] = []

    for row in csv_reader:
        x.append(x_type(row[x_label]))
        y.append(y_type(row[y_label]))

# Create the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color="blue", alpha=0.6)

# Add labels and title
plt.xlabel(x_label)
plt.ylabel(y_label)
# plt.title('2D Scatter Plot')

# Add a grid
plt.grid(True, linestyle="--", alpha=0.7)

# Show the plot
plt.show()

pass
