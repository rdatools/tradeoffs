#!/usr/bin/env python3

"""
GENERATE THE WORKFLOW FOR A STATE

For example:

$ scripts/make_workflow.py \
--state NC \
--no-debug \
> workflows/NC.sh

For documentation, type:

$ scripts/make_workflow.py

"""

import argparse
from argparse import ArgumentParser, Namespace

from typing import Dict, Any

from rdabase import require_args


def main() -> None:
    """Generate the workflow for a state.

    The end-to-end process

    - Copy notable map BAF's from pg/data -- DONE en masse 02/20/24
    - Copy ratings tables from pg/docs/_data -- DONE en masse 02/20/24

    - Generate an ensemble of 100 random plans
    - Approximate a root map with them
    - Generate 10K random plans, using ReCom and the root map as the starting plan
    - Score the plans in the ensemble
    - Find the frontiers

    - Flatten the scorecard for a focus map of interest (e.g., the official map) <<< TODO

    - Generate push_plan jobs <<< TODO
    - Push the frontiers <= parallelize <<< TODO
    - Append the pushed plans to a copy of the original ensemble <<< TODO

    - Find the new frontiers
    - Add the plans for any new frontier points to the original ensemble <<< TODO - Todd?
    - ID the notable maps in the augmented ensemble

    - Make a box plot
    - Make a statistics table <<< TODO - Including pushed points?
    - Make a notable maps ratings table
    - Make scatter plots w/ pre-/post-push frontiers

    """

    args: argparse.Namespace = parse_args()

    xx: str = args.state

    pass  # TODO


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
        "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
    )

    # Enable debug/explicit mode
    parser.add_argument("--debug", default=True, action="store_true", help="Debug mode")
    parser.add_argument(
        "--no-debug", dest="debug", action="store_false", help="Explicit mode"
    )

    args: Namespace = parser.parse_args()

    # Default values for args in debug mode
    debug_defaults: Dict[str, Any] = {
        "state": "NC",
        "verbose": True,
    }
    args = require_args(args, args.debug, debug_defaults)

    return args


if __name__ == "__main__":
    main()

### END ###
