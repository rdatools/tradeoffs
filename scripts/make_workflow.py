#!/usr/bin/env python3

"""
GENERATE THE WORKFLOW FOR A STATE

For example:

$ scripts/make_workflow.py --state NC > workflows/NC.sh

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

    print(f"### Workflows for {xx} ###")
    print()
    print(
        f"# Make sure you have done Steps 1-3 in the overall [workflow description](https://rdatools.github.io/tradeoffs/workflow)"
    )
    print()
    print()

    for i, plan_type in enumerate(["congress", "upper", "lower"]):
        print(f"## Commands for '{plan_type}'")
        print()
        print(f"# From 'rdaensemble'")
        print(f"scripts/STEP_5.sh --state {xx} --plan-type {plan_type}")
        print()
        print(f"# From 'rdaensemble'")
        print(f"scripts/STEP_6.sh --state {xx} --plan-type {plan_type}")
        print()
        print(f"# From 'tradeoffs'")
        print(f"scripts/STEP_7.sh --state {xx} --plan-type {plan_type}")
        print()
        print()

    print(
        f"# Make sure you do Steps 8 & 9 in the overall [workflow description](https://rdatools.github.io/tradeoffs/workflow)"
    )
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

    args: Namespace = parser.parse_args()

    return args


if __name__ == "__main__":
    main()

### END ###
