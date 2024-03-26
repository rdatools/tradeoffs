#!/usr/bin/env python3

"""
PUSH PROPORTIONALITY == 0 PLANS IN SC ENSEMBLE

To run:

$ scripts/special_south_carolina.py

"""

import argparse
from argparse import ArgumentParser, Namespace

from typing import List, Dict, Tuple, Set, Any

import warnings

warnings.warn = lambda *args, **kwargs: None

from csv import DictReader

from rdabase import (
    cycle,
    plan_type,
    load_metadata,
    starting_seed,
    read_json,
    write_csv,
)
from rdaensemble.general import ratings_dimensions
from tradeoffs import GeoID, DistrictID, Name, Weight


def read_scores(
    scores_csv: str,
) -> List[Dict]:
    """Read a scores CSV file & filter out the unrealistic plans."""

    ratings: List[Dict] = []
    with open(scores_csv, "r", encoding="utf-8-sig") as f:
        reader: DictReader[str] = DictReader(
            f, fieldnames=None, restkey=None, restval=None, dialect="excel"
        )
        for row in reader:
            name: str = row["map"]
            plan_ratings: List[int | float] = [int(row[d]) for d in ratings_dimensions]
            ratings.append({"name": name, "ratings": plan_ratings})

    return ratings


def main() -> None:
    """Make special South Carolina push jobs."""

    args: argparse.Namespace = parse_args()

    ### BEGIN CUSTOM SC CODE ###

    args.state = "SC"
    args.plans = "../../iCloud/fileout/tradeoffs/SC/ensembles/SC20C_plans.json"
    args.scores = "../../iCloud/fileout/tradeoffs/SC/ensembles/SC20C_scores.csv"
    args.pin = True
    args.tolerance = 0.01
    args.saveatlimit = True
    args.pushes = 10
    args.cores = 28
    args.windfall = False
    args.data = "../rdabase/data/SC/SC_2020_data.csv"
    args.shapes = "../rdabase/data/SC/SC_2020_shapes_simplified.json"
    args.graph = "../rdabase/data/SC/SC_2020_graph.json"
    args.output = "../../iCloud/fileout/tradeoffs"
    args.verbose = True

    #

    xx: str = args.state
    xx_alt: str = "SC-alt"

    prefix: str = f"{args.state}{cycle[2:]}{plan_type[0]}"
    copy_path: str = f"{args.output}/{xx_alt}"
    run_path: str = f"~/dropbox/{xx}"
    run_path_alt: str = f"~/dropbox/{xx_alt}"

    ### END CUSTOM SC CODE ###

    # Load the metadata

    metadata: Dict[str, Any] = load_metadata(args.state, args.data)
    N: int = int(metadata["D"])
    start: int = starting_seed(args.state, N)

    # Load the ensemble of plans

    ensemble: Dict[str, Any] = read_json(args.plans)
    plans: List[Dict[str, Name | Weight | Dict[GeoID, DistrictID]]] = ensemble["plans"]
    plans_by_name: Dict[str, Dict[GeoID, DistrictID]] = {p["name"]: p["plan"] for p in plans}  # type: ignore

    ### BEGIN CUSTOM SC CODE ###

    # Load the scores

    plan_ratings: List[Dict] = read_scores(args.scores)

    # Make a list of plans to push

    plans_to_push: List[str] = []
    proportionality_index: int = ratings_dimensions.index("proportionality")
    for p in plan_ratings:
        if p["ratings"][proportionality_index] == 0:
            plans_to_push.append(p["name"])

    # Generate all the push commands

    pair: Tuple[str, ...] = ("proportionality", "minority")
    pin_mode: str = "proportionality"
    push_commands: List[Tuple[str, Tuple[str, ...], str, int]] = []

    for plan_name in plans_to_push:
        for i in range(args.pushes):
            push_commands.append((plan_name, pair, pin_mode, i))

    if args.verbose:
        print(f"# of push commands: {len(push_commands)}")

    ### END CUSTOM SC CODE ###

    # 'Chunk' the push commands into groups for a single node job

    pushes_per_job: List[List[Tuple[str, Tuple[str, ...], str, int]]] = []
    count: int = 0
    chunk: List[Tuple[str, Tuple[str, ...], str, int]] = []
    for push_command in push_commands:
        plan_name: str = push_command[0]
        pair: Tuple[str, ...] = push_command[1]
        pin_mode: str = push_command[2]
        i: int = push_command[3]
        chunk.append((plan_name, pair, pin_mode, i))
        count += 1
        if count % args.cores == 0:
            pushes_per_job.append(chunk)
            chunk = []
    if len(chunk) > 0:
        pushes_per_job.append(chunk)

    if args.verbose:
        print(f"# of jobs: {len(pushes_per_job)}")

    # Generate the jobs

    batch_copy: str = f"{copy_path}/submit_jobs.sh"
    with open(batch_copy, "w") as bf:
        print(f"chmod +x {run_path_alt}/jobs/*.sh", file=bf)
        seed: int = start
        plan_csv: Set[str] = set()

        for j, chunk in enumerate(pushes_per_job):  # for each job
            job_name: str = f"job_{j:04d}"
            job_copy: str = f"{copy_path}/jobs/{job_name}.sh"
            with open(job_copy, "w") as jf:
                for push_command in chunk:  # for each plan/command in the job
                    plan_name: str = push_command[0]
                    pair: Tuple[str, ...] = push_command[1]
                    pin_mode: str = push_command[2]
                    i: int = push_command[3]

                    dimensions: str = " ".join(pair)
                    x: str = str(ratings_dimensions.index(pair[1]) + 1)
                    y: str = str(ratings_dimensions.index(pair[0]) + 1)
                    z: str = (
                        str(ratings_dimensions.index(pin_mode) + 1) if pin_mode else "0"
                    )

                    plan_to_push: str = f"{prefix}_{plan_name}"
                    plan_copy: str = f"{copy_path}/plans/{plan_to_push}_plan.csv"
                    plan_run: str = f"{run_path_alt}/plans/{plan_to_push}_plan.csv"

                    pushed_prefix: str = prefix + f"_{plan_name}_{y}{x}{z}"

                    if plan_name not in plan_csv:
                        plan: List[Dict] = [
                            {"GEOID": k, "DISTRICT": v}
                            for k, v in plans_by_name[plan_name].items()
                        ]

                        write_csv(plan_copy, plan, ["GEOID", "DISTRICT"])

                    pushed_run: str = pushed_prefix + f"_{i:02d}_plan.csv"
                    log_run: str = pushed_prefix + f"_{i:02d}_log.txt"

                    print(f"~/tradeoffs/scripts/push_plan.py \\", file=jf)
                    print(f"--state {xx} \\", file=jf)
                    print(f"--plan {plan_run} \\", file=jf)
                    print(f"--dimensions {dimensions} \\", file=jf)
                    if pin_mode:
                        print(f"--pin {pin_mode} \\", file=jf)
                        ### CUSTOM SC CODE ###
                        print(f"--tolerance {args.tolerance} \\", file=jf)
                    if args.saveatlimit:
                        print(f"--save-at-limit \\", file=jf)
                    print(f"--pushed {run_path_alt}/pushed/{pushed_run} \\", file=jf)
                    print(f"--log {run_path_alt}/pushed/{log_run} \\", file=jf)
                    print(f"--seed {seed} \\", file=jf)
                    print(f"--data {run_path}/data/data.csv \\", file=jf)
                    print(f"--shapes {run_path}/data/shapes.json \\", file=jf)
                    print(f"--graph {run_path}/data/graph.json \\", file=jf)
                    print(f"--verbose \\", file=jf)
                    print(f"--no-debug", file=jf)
                    print(f"###", file=jf)

                    seed += 1

            run_mode: str = "windall" if args.windfall else "standard"
            slurm_copy: str = f"{copy_path}/jobs/{job_name}.slurm"
            with open(slurm_copy, "w") as sf:
                print(f"#!/bin/bash", file=sf)
                print(f"", file=sf)
                print(f"#SBATCH --ntasks={args.cores}", file=sf)
                print(f"#SBATCH --nodes=1", file=sf)
                print(f"#SBATCH --time=00:20:00", file=sf)
                print(f"#SBATCH --partition={run_mode}", file=sf)
                print(f"#SBATCH --account=proebsting", file=sf)
                print(f"#SBATCH -o dropbox/{xx_alt}/pushed/{job_name}.out", file=sf)
                print(f"", file=sf)
                print(f"module load parallel", file=sf)
                print(f"module load python/3.11", file=sf)
                print(f"source ~/venv/bin/activate", file=sf)
                print(f'export PYTHONPATH="$PYTHONPATH":~/tradeoffs', file=sf)
                print(f"", file=sf)
                print(
                    f"cat {run_path_alt}/jobs/{job_name}.sh | parallel -d '###' --joblog dropbox/{xx_alt}/pushed/{job_name}.log",
                    file=sf,
                )

            print(f"sbatch {run_path_alt}/jobs/{job_name}.slurm", file=bf)


def parse_args():
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Make special South Carolina push jobs."
    )

    parser.add_argument(
        "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
    )

    args: Namespace = parser.parse_args()

    return args


if __name__ == "__main__":
    main()

### END ###
