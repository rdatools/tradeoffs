#!/usr/bin/env python3

"""
MAKE "PUSH" JOBS FOR EACH POINT IN THE FRONTIERS FOR AN ENSEMBLE

For example:

$ scripts/make_push_jobs.py \
--state NC \
--plans ../../iCloud/fileout/ensembles/NC20C_plans.json \
--frontier ../../iCloud/fileout/ensembles/NC20C_frontiers.json \
--multiplier 1 \
--data ../rdabase/data/NC/NC_2020_data.csv \
--shapes ../rdabase/data/NC/NC_2020_shapes_simplified.json \
--graph ../rdabase/data/NC/NC_2020_graph.json \
--intermediate ../../iCloud/fileout/intermediate \
--output ../../iCloud/fileout/hpc_batch \
--no-debug

For documentation, type:

$ scripts/make_push_jobs.py

"""

import argparse
from argparse import ArgumentParser, Namespace

from typing import List, Dict, Any

import os
import shutil

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
    """Copy the support files & create a push 'job' for each point in each frontier in an ensemble."""

    args: argparse.Namespace = parse_args()

    xx: str = args.state

    prefix: str = f"{args.state}{cycle[2:]}{plan_type[0]}"
    copy_path: str = f"{args.output}/{xx}"
    run_path: str = f"home/{xx}"  # TODO

    # Copy the 3 state input files

    shutil.copy(args.data, os.path.join(f"{copy_path}/data", "data.csv"))
    shutil.copy(args.shapes, os.path.join(f"{copy_path}/data", "shapes.json"))
    shutil.copy(args.graph, os.path.join(f"{copy_path}/data", "graph.json"))

    # Copy the push_plan.py script

    shutil.copy(
        "scripts/push_plan.py", os.path.join(f"{copy_path}/jobs", "push_plan.py")
    )  # TODO - Make this standalone?

    # Create each push job

    metadata: Dict[str, Any] = load_metadata(args.state, args.data)
    N: int = int(metadata["D"])
    seed: int = starting_seed(args.state, N)

    ensemble: Dict[str, Any] = read_json(args.plans)
    plans: List[Dict[str, Name | Weight | Dict[GeoID, DistrictID]]] = ensemble["plans"]
    plans_by_name: Dict[str, Dict[GeoID, DistrictID]] = {p["name"]: p["plan"] for p in plans}  # type: ignore

    frontiers_blob: Dict[str, Any] = read_json(args.frontier)
    frontiers: Dict[str, Any] = frontiers_blob["frontiers"]

    for k, v in frontiers.items():  # for each frontier
        dimensions: str = " ".join(k.split("_"))

        for i, p in enumerate(v):  # for each point
            name: str = p["map"]
            plan: List[Dict] = [
                {"GEOID": k, "DISTRICT": v} for k, v in plans_by_name[name].items()
            ]

            plan_to_push: str = f"{prefix}_{name}"
            plan_copy: str = f"{copy_path}/plans/{plan_to_push}_plan.csv"
            plan_run: str = f"{run_path}/plans/{plan_to_push}_plan.csv"

            pushed_prefix: str = prefix + f"_{k}_{i:02d}"
            log_run: str = f"{plan_to_push}_log.txt"

            write_csv(plan_copy, plan, ["GEOID", "DISTRICT"])

            job_copy: str = f"{copy_path}/jobs/{plan_to_push}_job.sh"
            with open(job_copy, "w") as f:
                for _ in range(1, args.mutiplier + 1):  # for each multiple
                    # TODO
                    # pushed_plan = pair + i + seed <<< assert pt_index <= 100
                    # pushed_file = prefix + pushed_plan

                    print(f"push_plan.py \\", file=f)
                    print(f"--state {xx} \\", file=f)
                    print(f"--plan {plan_run} \\", file=f)
                    print(f"--dimensions {dimensions} \\", file=f)
                    print(f"--seed {seed} \\", file=f)
                    print(f"--iteration {args.multiplier} \\", file=f)
                    print(f"--prefix {pushed_prefix} \\", file=f)
                    print(f"--data {run_path}/data/data.csv \\", file=f)
                    print(f"--shapes {run_path}/data/shapes.json \\", file=f)
                    print(f"--graph {run_path}/data/graph.json \\", file=f)
                    print(f"--output {run_path}/data/pushed \\", file=f)
                    print(f"--log {run_path}/jobs/{log_run} \\", file=f)
                    print(f"--verbose \\", file=f)
                    print(f"--no-debug", file=f)

                    seed += 1


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
        "plans": "../../iCloud/fileout/ensembles/NC20C_plans.json",
        "frontier": "../../iCloud/fileout/ensembles/NC20C_frontiers.json",
        "multiplier": 1,  # TODO
        "data": "../rdabase/data/NC/NC_2020_data.csv",
        "shapes": "../rdabase/data/NC/NC_2020_shapes_simplified.json",
        "graph": "../rdabase/data/NC/NC_2020_graph.json",
        "intermediate": "../../iCloud/fileout/intermediate",  # TODO
        "output": "../../iCloud/fileout/hpc_batch",
        "verbose": True,
    }
    args = require_args(args, args.debug, debug_defaults)

    return args


if __name__ == "__main__":
    main()

### END ###
