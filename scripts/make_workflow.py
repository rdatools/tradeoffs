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

    ensembles_dir: str = "ensembles"
    if plan_type in ["upper", "lower"]:
        ensembles_dir = f"{ensembles_dir}-{plan_type}"

    prefix: str = f"{args.state}{cycle[2:]}{plan_type[0].capitalize()}"

    #

    print(f"### Workflow for {xx}-{plan_type} ###")
    print()
    print(
        f"For details on the manual Step 3, see https://rdatools.github.io/tradeoffs/workflow."
    )
    print()
    print(f"( ) Step 1 - Extract the data, shapes, and graph for the state")
    print()
    print(f"( ) Step 2 - Set up the state for trade-off analysis (once per state)")
    print(f"    From 'tradeoffs' run:")
    print()
    print(f"    scripts/setup_state {xx}")
    print()
    print(f"( ) Step 3 - Manual steps")
    print(f"    * First, verify the notable maps copied from DRA.")
    print(
        f"    * Then, in DRA create a proxy of the official map that doesn't any split precincts."
    )
    print()
    print(f"( ) Step 4 - Generate & score an unbiased ensemble")
    print(f"    From 'rdaensemble' run:")
    print()
    print(
        f"    scripts/make_and_score_ensemble.sh --state {xx} --plantype {plan_type} --size {args.size}"
    )
    print(f"    scripts/pack-zip_ensemble.sh --state {xx} --plantype {plan_type}")
    print()
    print(f"( ) Step 5 - Find the trade-off frontiers for the unbiased ensemble")
    print(f"    From 'tradeoffs' run:")
    print()
    print(
        f"    scripts/find_frontiers.sh --state {xx} --plantype {plan_type} > ../../temp/tradeoffs/{xx}/{ensembles_dir}/{prefix}_scores_notes.txt"
    )
    print()
    print(f"( ) Step 6 - 'Push' the frontiers of the unbiased ensemble")
    print(f"    From 'rdaensemble' run:")
    print()
    print(f"    scripts/push_frontiers.sh --state {xx} --plantype {plan_type}")
    print()
    print(f"( ) Step 7 - Make the analysis artifacts")
    print(f"    From 'tradeoffs' run:")
    print()
    print(f"    scripts/make_artifacts.sh --state {xx} --plantype {plan_type}")
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
    parser.add_argument(
        "--size",
        type=int,
        default=10000,
        help="The number of plans to keep in the ensemble",
    )

    args: Namespace = parser.parse_args()

    return args


if __name__ == "__main__":
    main()

### END ###
