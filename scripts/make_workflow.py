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

from rdabase import require_args, cycle


def main() -> None:
    """Generate the workflows for a state."""

    args: argparse.Namespace = parse_args()

    xx: str = args.state
    plan_type: str = args.type
    assert plan_type in ["congress", "upper", "lower"]

    prefix: str = f"{args.state}{cycle[2:]}{plan_type[0].capitalize()}"

    #

    print(f"### Workflow for {xx}-{plan_type} ###")
    print()
    print(
        f"For details on the manual data gather https://rdatools.github.io/tradeoffs/workflow."
    )
    print()
    print(f"( ) Step 1 - Extract the data, shapes, and graph for the state")
    print()
    print(f"( ) Step 2 - Set up the state for trade-off analysis (once per state)")
    print(f"    From 'tradeoffs' run:")
    print()
    print(f"    scripts/setup_state {xx}")
    print()
    print(f"( ) Step 3 - Gather additional data points manually")
    print()
    print(f"( ) Step 4 - Generate & score an unbiased ensemble")
    print(f"    From 'rdaensemble' run:")
    print()
    print(
        f"    scripts/make_and_score_ensemble.sh --state {xx} --plan-type {plan_type}"
    )
    print()
    print(f"( ) Step 5 - Find the trade-off frontiers for the unbiased ensemble")
    print(f"    From 'tradeoffs' run:")
    print()
    print(
        f"    scripts/find_frontiers.sh --state {xx} --plan-type {plan_type} > ../tradeoffs-dropbox/scores/{prefix}_scores_notes.txt"
    )
    print()
    print(f"( ) Step 6 - 'Push' the frontiers of the unbiased ensemble")
    print(f"    From 'rdaensemble' run:")
    print()
    print(f"    scripts/push_frontiers.sh --state {xx} --plan-type {plan_type}")
    print()
    print(f"( ) Step 7 - Make the analysis artifacts")
    print(f"    From 'tradeoffs' run:")
    print()
    print(f"    scripts/make_artifacts.sh --state {xx} --plan-type {plan_type}")
    print()
    print(f"( ) Step 8 - Deploy the state (once per state)")
    print(f"    From 'tradeoffs' run:")
    print()
    print(f"    scripts/deploy_state.sh {xx}")
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
