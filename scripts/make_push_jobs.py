#!/usr/bin/env python3

"""
MAKE "PUSH" JOBS FOR EACH POINT IN THE FRONTIERS FOR AN ENSEMBLE

For example:

$ scripts/make_push_jobs.py \
--state NC \
--plans ../../iCloud/fileout/ensembles/NC20C_plans.json \
--frontier ../../iCloud/fileout/ensembles/NC20C_frontiers.json \
--multiplier 28 \
--data ../rdabase/data/NC/NC_2020_data.csv \
--shapes ../rdabase/data/NC/NC_2020_shapes_simplified.json \
--graph ../rdabase/data/NC/NC_2020_graph.json \
--output ../../iCloud/fileout/hpc_dropbox \
--no-debug

For documentation, type:

$ scripts/make_push_jobs.py

"""

import argparse
from argparse import ArgumentParser, Namespace

from typing import List, Dict, Tuple, Any

import os
import shutil
import itertools

from rdabase import (
    require_args,
    cycle,
    plan_type,
    load_metadata,
    starting_seed,
    read_json,
    write_csv,
)
from rdaensemble.general import ratings_dimensions
from tradeoffs import GeoID, DistrictID, Name, Weight


def main() -> None:
    """Copy the support files & create a push 'job' for each point in each frontier in an ensemble."""

    args: argparse.Namespace = parse_args()

    xx: str = args.state

    prefix: str = f"{args.state}{cycle[2:]}{plan_type[0]}"
    copy_path: str = f"{args.output}/{xx}"
    run_path: str = f"$HOME/dropbox/{xx}"

    # Copy the 3 state input files

    shutil.copy(args.data, os.path.join(f"{copy_path}/data", "data.csv"))
    shutil.copy(args.shapes, os.path.join(f"{copy_path}/data", "shapes.json"))
    shutil.copy(args.graph, os.path.join(f"{copy_path}/data", "graph.json"))

    # Copy the standalone push_plan executable

    shutil.copy("scripts/push_plan", os.path.join(f"{copy_path}/jobs", "push_plan"))

    # Create each push job

    metadata: Dict[str, Any] = load_metadata(args.state, args.data)
    N: int = int(metadata["D"])
    start: int = starting_seed(args.state, N)

    ensemble: Dict[str, Any] = read_json(args.plans)
    plans: List[Dict[str, Name | Weight | Dict[GeoID, DistrictID]]] = ensemble["plans"]
    plans_by_name: Dict[str, Dict[GeoID, DistrictID]] = {p["name"]: p["plan"] for p in plans}  # type: ignore

    frontiers_blob: Dict[str, Any] = read_json(args.frontier)
    frontiers: Dict[str, Any] = frontiers_blob["frontiers"]

    ratings_pairs: List = list(itertools.combinations(ratings_dimensions, 2))

    batch_copy: str = f"{copy_path}/submit_jobs.sh"
    with open(batch_copy, "w") as bf:
        print(f"chmod +x {run_path}/jobs/*.sh", file=bf)
        # print(f"chmod +x {run_path}/jobs/*.slurm", file=bf)

        for k, v in frontiers.items():  # for each frontier
            dimensions: str = " ".join(k.split("_"))

            pair: Tuple[str, ...] = tuple(k.split("_"))
            y: str = str(ratings_dimensions.index(pair[0]) + 1)
            x: str = str(ratings_dimensions.index(pair[1]) + 1)

            for i, p in enumerate(v):  # for each point
                name: str = p["map"]
                plan: List[Dict] = [
                    {"GEOID": k, "DISTRICT": v} for k, v in plans_by_name[name].items()
                ]

                plan_to_push: str = f"{prefix}_{name}"
                plan_copy: str = f"{copy_path}/plans/{plan_to_push}_plan.csv"
                plan_run: str = f"{run_path}/plans/{plan_to_push}_plan.csv"

                pushed_prefix: str = prefix + f"_{name}_{y}{x}"

                write_csv(plan_copy, plan, ["GEOID", "DISTRICT"])

                job_copy: str = f"{copy_path}/jobs/{plan_to_push}.sh"
                seed: int = start
                with open(job_copy, "w") as jf:
                    for j in range(1, args.multiplier + 1):  # for each multiple
                        pushed_run: str = pushed_prefix + f"_{j:03d}_plan.csv"
                        log_run: str = pushed_prefix + f"_{j:03d}_log.txt"

                        print(f"push_plan \\", file=jf)
                        print(f"--state {xx} \\", file=jf)
                        print(f"--plan {plan_run} \\", file=jf)
                        print(f"--dimensions {dimensions} \\", file=jf)
                        print(f"--pushed {run_path}/pushed/{pushed_run} \\", file=jf)
                        print(f"--log {run_path}/pushed/{log_run} \\", file=jf)
                        print(f"--seed {seed} \\", file=jf)
                        print(f"--data {run_path}/data/data.csv \\", file=jf)
                        print(f"--shapes {run_path}/data/shapes.json \\", file=jf)
                        print(f"--graph {run_path}/data/graph.json \\", file=jf)
                        print(f"--verbose \\", file=jf)
                        print(f"--no-debug", file=jf)
                        print(f"###", file=jf)

                        seed += 1

                slurm_copy: str = f"{copy_path}/jobs/{plan_to_push}.slurm"
                with open(slurm_copy, "w") as sf:
                    print(f"#!/bin/bash", file=sf)
                    print(f"", file=sf)
                    print(f"#SBATCH --ntasks=28", file=sf)
                    print(f"#SBATCH --nodes=1", file=sf)
                    print(f"#SBATCH --time=00:10:00", file=sf)
                    print(f"#SBATCH --partition=standard", file=sf)
                    print(f"#SBATCH --account=proebsting", file=sf)
                    print(f"#SBATCH -o {plan_to_push}.out", file=sf)
                    print(f"", file=sf)
                    print(f"module load parallel", file=sf)
                    print(f"module load python/3.11", file=sf)
                    print(f"", file=sf)
                    print(
                        f"cat {run_path}/jobs/{plan_to_push}.sh | parallel -d '###'",
                        file=sf,
                    )

                print(f"sbatch {run_path}/jobs/{plan_to_push}.slurm", file=bf)


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
        "multiplier": 1,
        "data": "../rdabase/data/NC/NC_2020_data.csv",
        "shapes": "../rdabase/data/NC/NC_2020_shapes_simplified.json",
        "graph": "../rdabase/data/NC/NC_2020_graph.json",
        "output": "../../iCloud/fileout/hpc_dropbox",
        "verbose": True,
    }
    args = require_args(args, args.debug, debug_defaults)

    return args


if __name__ == "__main__":
    main()

### END ###
