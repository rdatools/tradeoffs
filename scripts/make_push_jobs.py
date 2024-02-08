#!/usr/bin/env python3

"""
MAKE "PUSH" JOBS FOR EACH POINT IN THE FRONTIERS FOR AN ENSEMBLE

For example:

$ scripts/make_push_jobs.py \
--state NC \
--plans ../../iCloud/fileout/ensembles/NC20C_ReCom_1K_plans.json \
--frontier ../../iCloud/fileout/ensembles/NC20C_ReCom_1K_frontiers.json \
--multiplier 1 \
--data ../rdabase/data/NC/NC_2020_data.csv \
--shapes ../rdabase/data/NC/NC_2020_shapes_simplified.json \
--graph ../rdabase/data/NC/NC_2020_graph.json \
--intermediate ../../iCloud/fileout/intermediate \
--output ../../iCloud/fileout/temp \
--no-debug \
> run_batch.sh

For documentation, type:

$ scripts/make_push_jobs.py

"""

import argparse
from argparse import ArgumentParser, Namespace

from typing import List, Dict, Any

import os

from rdabase import (
    require_args,
    cycle,
    plan_type,
    load_metadata,
    starting_seed,
    read_json,
    write_csv,
)
from tradeoffs import GeoID, DistrictID, Name, Weight


def main() -> None:
    """Make a 'job' for each point in each frontier in an ensemble."""

    args: argparse.Namespace = parse_args()

    xx: str = args.state
    prefix: str = f"{args.state}{cycle[2:]}{plan_type[0]}"

    metadata: Dict[str, Any] = load_metadata(args.state, args.data)
    N: int = int(metadata["D"])
    seed: int = starting_seed(args.state, N)

    ensemble: Dict[str, Any] = read_json(args.plans)
    plans: List[Dict[str, Name | Weight | Dict[GeoID, DistrictID]]] = ensemble["plans"]
    plans_by_name: Dict[str, Dict[GeoID, DistrictID]] = {p["name"]: p["plan"] for p in plans}  # type: ignore

    frontiers_blob: Dict[str, Any] = read_json(args.frontier)
    frontiers: Dict[str, Any] = frontiers_blob["frontiers"]

    print(
        f"# Command-line calls to 'push' points in {os.path.expanduser(args.frontier)}."
    )
    print(
        f"# - The input plans have been written to {os.path.expanduser(args.intermediate)}/."
    )
    print(
        f"# - The supporting data, shapes, & graph must be in {os.path.dirname(os.path.expanduser(args.data))}/."
    )
    print(
        f"# - The output plans will be written to {os.path.expanduser(args.output)}/."
    )
    print()

    for k, v in frontiers.items():
        dimensions: str = " ".join(k.split("_"))

        for i, p in enumerate(v):
            name: str = p["map"]
            plan: List[Dict] = [
                {"GEOID": k, "DISTRICT": v} for k, v in plans_by_name[name].items()
            ]

            plan_to_push: str = f"{prefix}_{name}"
            plan_path: str = os.path.expanduser(
                f"{args.intermediate}/{plan_to_push}_plan.csv"
            )

            pushed_prefix: str = prefix + f"_{k}_{i:02d}"
            log_path: str = f"{args.output}/{plan_to_push}_log.txt"

            write_csv(plan_path, plan, ["GEOID", "DISTRICT"])

            print(f"scripts/push_plan.py \\")
            print(f"--state {xx} \\")
            print(f"--plan {plan_path} \\")
            print(f"--dimensions {dimensions} \\")
            print(f"--seed {seed} \\")
            print(f"--multiplier {args.multiplier} \\")
            print(f"--prefix {pushed_prefix} \\")
            print(f"--data {os.path.expanduser(args.data)} \\")
            print(f"--shapes {os.path.expanduser(args.shapes)} \\")
            print(f"--graph {os.path.expanduser(args.graph)} \\")
            print(f"--output {os.path.expanduser(args.output)} \\")
            print(f"--log {os.path.expanduser(log_path)} \\")
            print(f"--verbose \\")
            print(f"--no-debug")
            print()


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
    parser.add_argument(
        "--intermediate",
        type=str,
        help="Directory to write input plan CSV's to",
    )
    parser.add_argument(
        "--output",
        type=str,
        help="Directory to write 'pushed' plan CSV's to",
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
        "plans": "../../iCloud/fileout/ensembles/NC20C_ReCom_1K_plans.json",
        "frontier": "../../iCloud/fileout/ensembles/NC20C_ReCom_1K_frontiers.json",
        "multiplier": 1,
        "data": "../rdabase/data/NC/NC_2020_data.csv",
        "shapes": "../rdabase/data/NC/NC_2020_shapes_simplified.json",
        "graph": "../rdabase/data/NC/NC_2020_graph.json",
        "intermediate": "../../iCloud/fileout/intermediate",
        "output": "../../iCloud/fileout/temp",
        "verbose": True,
    }
    args = require_args(args, args.debug, debug_defaults)

    return args


if __name__ == "__main__":
    main()

### END ###
