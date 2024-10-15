#!/usr/bin/env python3

"""
ANALYZE THE LOG OF GAPS BETWEEN SAMPLES
"""

import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from typing import cast


def extract_ids(text):
    # Regular expression to match the IDs in parentheses
    pattern = r"\((\d+)\)"

    # Find all matches in the text
    matches = re.findall(pattern, text)

    # Return the list of IDs
    return matches


def format_output(ids):
    # Create the header
    output = "ID\n"

    # Add each ID on a new line
    for id in ids:
        output += f"{id}\n"

    return output


def read_file(filename):
    with open(filename, "r") as file:
        return file.read()


def main():
    """
    log_file = "../../iCloud/fileout/tradeoffs/NC/analysis/unique_plans_log.txt"

    # Read the file
    input_text = read_file(log_file)

    # Extract the IDs
    extracted_ids = extract_ids(input_text)

    # Format the output
    formatted_output = format_output(extracted_ids)

    # Print the output
    print(formatted_output)
    """

    # Read the CSV file
    df = pd.read_csv("../../iCloud/fileout/tradeoffs/NC/analysis/kept_plans.csv")

    # Convert IDs to integers and calculate the differences
    df["ID"] = df["ID"].astype(int)
    df["Gap"] = df["ID"].diff()

    # Remove the first row (which will have a NaN gap)
    df = df.dropna()

    # Create a sequence for the x-axis (gap number)
    df["GapNumber"] = range(1, len(df) + 1)

    # Plot the data
    plt.figure(figsize=(12, 6))
    plt.scatter(df["GapNumber"], df["Gap"], alpha=0.5)

    # Calculate and plot the best fit line
    slope, intercept, r_value, p_value, std_err = stats.linregress(
        df["GapNumber"], df["Gap"]
    )
    x = np.array(df["GapNumber"])
    line = slope * x + intercept
    r_value_float = cast(float, r_value)  # Cast r_value to float
    plt.plot(x, line, color="r", label=f"Best fit line (R² = {r_value_float**2:.3f})")

    plt.xlabel("Gap Sequence")
    plt.ylabel("Gap Magnitude")
    plt.title("Sequence of Gaps between Successive IDs")
    plt.legend()

    # Add grid for better readability
    plt.grid(True, linestyle="--", alpha=0.7)

    # Show the plot
    plt.tight_layout()
    plt.show()

    # Print some basic statistics
    print(f"Average gap: {df['Gap'].mean():.2f}")
    print(f"Median gap: {df['Gap'].median():.2f}")
    print(f"Minimum gap: {df['Gap'].min():.2f}")
    print(f"Maximum gap: {df['Gap'].max():.2f}")

    pass


if __name__ == "__main__":
    main()

### END ###
