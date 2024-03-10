#!/usr/bin/env python3

"""
MAKE "PUSH" JOBS FOR EACH POINT IN THE FRONTIERS FOR AN ENSEMBLE

For example:

$ scripts/make_push_jobs.py \
--state NC \
--plans ../../iCloud/fileout/ensembles/NC20C_plans.json \
--scores ../../iCloud/fileout/ensembles/NC20C_scores.csv \
--frontier ../../iCloud/fileout/ensembles/NC20C_frontiers.json \
--points 100 \
--pushes 3 \
--cores 28 \
--data ../rdabase/data/NC/NC_2020_data.csv \
--shapes ../rdabase/data/NC/NC_2020_shapes_simplified.json \
--graph ../rdabase/data/NC/NC_2020_graph.json \
--output ../../iCloud/fileout/hpc_dropbox \
--no-debug

$ scripts/make_push_jobs.py \
--state NC \
--plans ../../iCloud/fileout/ensembles/NC20C_plans.json \
--scores ../../iCloud/fileout/ensembles/NC20C_scores.csv \
--frontier ../../iCloud/fileout/ensembles/NC20C_frontiers.json \
--zone \
--points 100 \
--pushes 3 \
--cores 28 \
--data ../rdabase/data/NC/NC_2020_data.csv \
--shapes ../rdabase/data/NC/NC_2020_shapes_simplified.json \
--graph ../rdabase/data/NC/NC_2020_graph.json \
--output ../../iCloud/fileout/hpc_dropbox \
--no-debug

$ scripts/make_push_jobs.py \
--state NC \
--plans ../../iCloud/fileout/ensembles/NC20C_plans.json \
--scores ../../iCloud/fileout/ensembles/NC20C_scores.csv \
--frontier ../../iCloud/fileout/ensembles/NC20C_frontiers.json \
--random \
--points 100 \
--pushes 3 \
--cores 28 \
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

import warnings

warnings.warn = lambda *args, **kwargs: None

import os
import shutil
import random

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
from tradeoffs import GeoID, DistrictID, Name, Weight, read_ratings, is_near_any


def main() -> None:
    """Copy the support files & create a push 'job' for each point in each frontier in an ensemble."""

    args: argparse.Namespace = parse_args()

    xx: str = args.state

    prefix: str = f"{args.state}{cycle[2:]}{plan_type[0]}"
    copy_path: str = f"{args.output}/{xx}"
    run_path: str = f"~/dropbox/{xx}"

    # Copy the 3 state input files

    shutil.copy(args.data, os.path.join(f"{copy_path}/data", "data.csv"))
    shutil.copy(args.shapes, os.path.join(f"{copy_path}/data", "shapes.json"))
    shutil.copy(args.graph, os.path.join(f"{copy_path}/data", "graph.json"))

    metadata: Dict[str, Any] = load_metadata(args.state, args.data)
    N: int = int(metadata["D"])
    start: int = starting_seed(args.state, N)

    # Load the ensemble of plans

    ensemble: Dict[str, Any] = read_json(args.plans)
    plans: List[Dict[str, Name | Weight | Dict[GeoID, DistrictID]]] = ensemble["plans"]
    plans_by_name: Dict[str, Dict[GeoID, DistrictID]] = {p["name"]: p["plan"] for p in plans}  # type: ignore

    # Load the frontier points

    frontiers_blob: Dict[str, Any] = read_json(args.frontier)
    frontiers: Dict[str, Any] = frontiers_blob["frontiers"]

    # Make a list of plans to push for each pair of ratings dimensions
    # Always push all the points on the frontiers

    plans_by_pair: Dict[str, List[str]] = {}
    for k, v in frontiers.items():  # for each frontier
        plans_by_pair[k] = []
        for p in v:  # for each point
            name: str = p["map"]
            plans_by_pair[k].append(name)

    # Also optionally push additional random plans up to a limit

    if args.zone or args.random:
        plan_ratings: List[Dict] = read_ratings(args.scores, verbose=args.verbose)

        # Either push random plans in the 'zone' near the frontier
        if args.zone:
            zone_plans: Dict[str, List[str]] = get_zone_plans(
                frontiers, plan_ratings, args.delta
            )
            for k, _ in frontiers.items():
                while len(plans_by_pair[k]) < args.points and len(zone_plans[k]) > 0:
                    name: str = random.choice(zone_plans[k])
                    zone_plans[k].remove(name)
                    if name not in plans_by_pair[k]:
                        plans_by_pair[k].append(name)

        # -or- push random plans
        if args.random:
            for k, _ in frontiers.items():
                while len(plans_by_pair[k]) < args.points:
                    name: str = random.choice(plan_ratings)["name"]
                    if name not in plans_by_pair[k]:
                        plans_by_pair[k].append(name)

    if args.verbose:
        print("Points to push by pair of ratings dimensions:")
        tf: int = 0
        tp: int = 0
        for k, v in frontiers.items():
            nf: int = len(v)
            np: int = len(plans_by_pair[k])

            tf += nf
            tp += np

            print(f"{k}: {nf} -> {np}")
        print(f"{k}: {tf} -> {tp}")

    # 'Chunk' the points to push into groups for a single node job

    plans_to_push: Dict[str, Tuple[str, ...]] = {}
    for k, v in plans_by_pair.items():
        pair: Tuple[str, ...] = tuple(k.split("_"))
        for n in v:
            plans_to_push[n] = pair

    pushes_per_job: List[List[Tuple[str, Tuple[str, ...]]]] = []
    count: int = 0
    commands: List[Tuple[str, Tuple[str, ...]]] = []
    for k, v in plans_to_push.items():
        commands.append((k, v))
        count += 1
        if count % args.cores == 0:
            pushes_per_job.append(commands)
            commands = []
    if len(commands) > 0:
        pushes_per_job.append(commands)

    # Generate the jobs

    batch_copy: str = f"{copy_path}/submit_jobs.sh"
    with open(batch_copy, "w") as bf:
        print(f"chmod +x {run_path}/jobs/*.sh", file=bf)
        job: int = 0
        seed: int = start

        for name, pair in plans_to_push.items():  # for each plan
            # name: str = p["map"]
            plan: List[Dict] = [
                {"GEOID": k, "DISTRICT": v} for k, v in plans_by_name[name].items()
            ]

            plan_to_push: str = f"{prefix}_{name}"
            plan_copy: str = f"{copy_path}/plans/{plan_to_push}_plan.csv"
            plan_run: str = f"{run_path}/plans/{plan_to_push}_plan.csv"

            pushed_prefix: str = prefix + f"_{name}_{y}{x}"

            write_csv(plan_copy, plan, ["GEOID", "DISTRICT"])

            job_copy: str = f"{copy_path}/jobs/{plan_to_push}.sh"

            with open(job_copy, "w") as jf:
                for j in range(1, args.cores + 1):  # for each multiple
                    pushed_run: str = pushed_prefix + f"_{j:03d}_plan.csv"
                    log_run: str = pushed_prefix + f"_{j:03d}_log.txt"

                    print(f"~/tradeoffs/scripts/push_plan.py \\", file=jf)
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
                print(f"#SBATCH --time=00:20:00", file=sf)
                print(f"#SBATCH --partition=standard", file=sf)
                print(f"#SBATCH --account=proebsting", file=sf)
                print(f"#SBATCH -o dropbox/{xx}/pushed/{plan_to_push}.out", file=sf)
                print(f"", file=sf)
                print(f"module load parallel", file=sf)
                print(f"module load python/3.11", file=sf)
                print(f"source ~/venv/bin/activate", file=sf)
                print(f'export PYTHONPATH="$PYTHONPATH":~/tradeoffs', file=sf)
                print(f"", file=sf)
                print(
                    f"cat {run_path}/jobs/{plan_to_push}.sh | parallel -d '###'",
                    file=sf,
                )

            print(f"sbatch {run_path}/jobs/{plan_to_push}.slurm", file=bf)


def get_zone_plans(
    frontiers: Dict[str, Any], plan_ratings: List[Dict], delta: int = 5
) -> Dict[str, List[str]]:
    """Get the plans in the 'zone' near the frontiers."""

    zone_plans: Dict[str, List[str]] = {}
    for k, v in frontiers.items():
        pair: Tuple[str, ...] = tuple(k.split("_"))
        ydim: str = pair[0]
        xdim: str = pair[1]
        d1: int = ratings_dimensions.index(ydim)
        d2: int = ratings_dimensions.index(xdim)

        zone_plans[k] = []
        frontier_points: List[Tuple[int, int]] = list(
            set([(p["ratings"][d2], p["ratings"][d1]) for p in v])
        )

        for plan in plan_ratings:
            name: str = plan["name"]
            pt: Tuple[int, int] = (plan["ratings"][d2], plan["ratings"][d1])

            if is_near_any(pt, frontier_points, delta=delta):
                zone_plans[k].append(name)

    return zone_plans


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
        "--scores",
        type=str,
        help="A CSV ensemble of scores including ratings to plot",
    )
    parser.add_argument(
        "--frontier",
        type=str,
        help="Frontier maps JSON file",
    )
    # TODO - These are mutually exclusive options, but I'm not defining them as such yet.
    parser.add_argument(
        "-z",
        "--zone",
        dest="zone",
        action="store_true",
        help="Push a 'zone' of points near the frontier and the frontier",
    )
    parser.add_argument(
        "-r",
        "--random",
        dest="random",
        action="store_true",
        help="Push a selection of random plans and the frontier",
    )
    parser.add_argument(
        "--points",
        type=int,
        default=100,
        help="The *maximum* number of points to push for each frontier.",
    )
    parser.add_argument(
        "--pushes",
        type=int,
        default=3,
        help="How many times to push each point.",
    )
    parser.add_argument("--cores", type=int, help="The number of core per node.")
    parser.add_argument(
        "--delta",
        type=int,
        default=5,
        help="How much ratings can differ for a point to be considered 'near' a frontier point",
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
        "scores": "../../iCloud/fileout/ensembles/NC20C_scores.csv",
        "frontier": "../../iCloud/fileout/ensembles/NC20C_frontiers.json",
        "zone": True,
        "random": False,
        "points": 100,
        "pushes": 3,
        "cores": 28,
        "delta": 5,
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
