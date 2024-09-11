#!/usr/bin/env python3

"""
GENERATE THE WORKFLOW FOR A STATE

For example:

$ scripts/make_workflow.py --state NC --type congress > workflows/NC-congress.txt
$ scripts/make_workflow.py --state NC --type upper > workflows/NC-upper.txt
$ scripts/make_workflow.py --state NC --type lower > workflows/NC-lower.txt

For documentation, type:

$ scripts/make_workflow.py -h
"""

import argparse
from argparse import ArgumentParser, Namespace

from typing import Dict, Any

from rdabase import require_args


def main() -> None:
    """Generate the workflows for a state."""

    args: argparse.Namespace = parse_args()

    xx: str = args.state
    plan_type: str = args.type
    assert plan_type in ["congress", "upper", "lower"]

    print(f"### Workflow for {xx}-{plan_type} ###")
    print()
    print(
        f"A detailed description of each step is in https://rdatools.github.io/tradeoffs/workflow."
    )
    print()
    print(f"( ) Step 1 - Extract the data, shapes, and graph for the state")
    print()
    print(f"( ) Step 2 - Set up the state for trade-off analysis")
    print()
    print(f"( ) Step 3 - Create an approximate 'root map'")
    print()
    print(f"( ) Step 4 - Gather additional data points manually")
    print()
    print(f"( ) Step 5 - Generate & score an unbiased ensemble")
    print(f"    From 'rdaensemble' run:")
    print()
    print(f"    scripts/STEP_5.sh --state {xx} --plan-type {plan_type}")
    print()
    print(f"( ) Step 6 - Generate & score an optimized ensemble")
    print(f"    From 'rdaensemble' run:")
    print()
    print(f"    scripts/STEP_6.sh --state {xx} --plan-type {plan_type}")
    print()
    print(
        f"( ) Step 7 - Find the trade-off frontiers & generate the analysis artifacts"
    )
    print(f"    From 'tradeoffs' run:")
    print()
    print(f"    scripts/STEP_7.sh --state {xx} --plan-type {plan_type}")
    print()
    print(f"( ) Step 8 - Deploy the artifacts")
    print()
    print(f"( ) Step 9 - Activate the state in the site")
    print()
    print(f"### END ###")


def parse_args():
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Generate the workflow for a state."
    )

    parser.add_argument(
        "--state",
        help="The two-character state code (e.g., NC)",
        type=str,
    )
    parser.add_argument(
        "--type",
        help="The type of plan (e.g., congress, upper, lower)",
        type=str,
    )

    args: Namespace = parser.parse_args()

    return args


if __name__ == "__main__":
    main()

### END ###
