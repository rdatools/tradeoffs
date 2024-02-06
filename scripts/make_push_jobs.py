#!/usr/bin/env python3

"""
MAKE "PUSH" JOBS FOR EACH POINT IN THE FRONTIERS FOR AN ENSEMBLE

For example:

$ scripts/make_push_jobs.py \
--state NC \
--plans ../../iCloud/fileout/ensembles/NC20C_ReCom_1000_plans.json \
--frontier ../../iCloud/fileout/ensembles/NC20C_ReCom_1000_frontiers.json \
--multiplier 1
--data ../rdabase/data/NC/NC_2020_data.csv \
--shapes ../rdabase/data/NC/NC_2020_shapes_simplified.json \
--graph ../rdabase/data/NC/NC_2020_graph.json \
--intermediate ../../iCloud/fileout/intermediate/ \
--output ../../iCloud/fileout/ensembles/temp/ \
--no-debug

For documentation, type:

$ scripts/make_push_jobs.py

"""

import argparse
from argparse import ArgumentParser, Namespace

from typing import List, Dict, Any

import itertools

from rdabase import require_args, read_json
from rdaensemble.general import ratings_dimensions
from tradeoffs import GeoID, DistrictID, Name, Weight


def main() -> None:
    """Make a 'job' for each point in each frontier in an ensemble."""

    args: argparse.Namespace = parse_args()

    ensemble: Dict[str, Any] = read_json(args.plans)
    plans: List[Dict[str, Name | Weight | Dict[GeoID, DistrictID]]] = ensemble["plans"]
    plans_by_name = {p["name"]: p["plan"] for p in plans}

    frontiers_blob: Dict[str, Any] = read_json(args.frontier)
    frontiers: Dict[str, Any] = frontiers_blob["frontiers"]

    for k, v in frontiers.items():
        print(f"Frontier: {k}:")
        for i, p in enumerate(v):
            # name: str = p["map"]  # type: ignore
            print(f"... point: {i}, map: {p['map']}")

            # TODO - Get the plan
            # TODO - Write it to disk (intermediate)
            # TODO - Generate the job to push the point

            pass

    pass


def parse_args():
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Make a ratings table (CSV) for the notable maps in an ensemble."
    )

    parser.add_argument(
        "--state",
        help="The two-character state code (e.g., NC)",
        type=str,
    )
    parser.add_argument(
        "--plans",
        type=str,
        help="Ensemble of plans to score in a JSON file",
    )
    parser.add_argument(
        "--frontier",
        type=str,
        help="Frontier maps JSON file",
    )
    parser.add_argument(
        "--multiplier", type=int, help="How many times to push each point"
    )
    #
    parser.add_argument(
        "--data",
        type=str,
        help="Data file",
    )
    parser.add_argument(
        "--shapes",
        type=str,
        help="Shapes abstract file",
    )
    parser.add_argument(
        "--graph",
        type=str,
        help="Graph file",
    )
    #
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
        "plans": "../../iCloud/fileout/ensembles/NC20C_ReCom_1000_plans.json",
        "frontier": "../../iCloud/fileout/ensembles/NC20C_ReCom_1000_frontiers.json",
        "multiplier": 1,
        "data": "../rdabase/data/NC/NC_2020_data.csv",
        "shapes": "../rdabase/data/NC/NC_2020_shapes_simplified.json",
        "graph": "../rdabase/data/NC/NC_2020_graph.json",
        "intermediate": "../../iCloud/fileout/intermediate/",
        "output": "../../iCloud/fileout/ensembles/temp/",
        "verbose": True,
    }
    args = require_args(args, args.debug, debug_defaults)

    return args


if __name__ == "__main__":
    main()

### END ###
