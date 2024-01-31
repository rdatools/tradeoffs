#!/usr/bin/env python3

"""
DEBUGG LOOPING - The Balzer looping

To run:

$ scripts/debug_looping.py

"""

import random

from typing import Any, List, Dict, Tuple, NamedTuple

from rdabase import require_args, read_json, starting_seed, write_json
from rdaensemble.general import (
    ratings_dimensions,
    plan_from_ensemble,
    make_plan,
    ensemble_metadata,
)
from rdascore import load_data, load_shapes, load_graph, load_metadata

from tradeoffs import (
    GeoID,
    DistrictID,
    DistrictOffset,
    Move,
    Mutation,
    Name,
    Weight,
    Plan,
    size_1_moves,
    push_point,
    Scorer,
)


class Args(NamedTuple):
    state: str
    plans: str
    frontier: str
    data: str
    shapes: str
    graph: str
    pushed: str
    multiplier: int
    verbose: bool
    debug: bool


def main() -> None:
    args: Args = Args(
        state="NC",
        plans="testdata/synthetic_plans.json",
        frontier="testdata/synthetic_frontier.json",
        data="../rdabase/data/NC/NC_2020_data.csv",
        shapes="../rdabase/data/NC/NC_2020_shapes_simplified.json",
        graph="../rdabase/data/NC/NC_2020_graph.json",
        pushed="output/test_pushed_plans.json",
        multiplier=1,
        verbose=True,
        debug=True,
    )

    # Load the data & shapes for scoring

    data: Dict[str, Dict[GeoID, DistrictID]] = load_data(args.data)
    shapes: Dict[str, Any] = load_shapes(args.shapes)
    graph: Dict[GeoID, List[GeoID]] = load_graph(args.graph)
    metadata: Dict[str, Any] = load_metadata(args.state, args.data)

    pop_by_geoid: Dict[GeoID, int] = {k: int(v["TOTAL_POP"]) for k, v in data.items()}

    frontiers: Dict[str, Any] = read_json(args.frontier)
    ensemble: Dict[str, Any] = read_json(args.plans)
    plans: List[Dict[str, Name | Weight | Dict[GeoID, DistrictID]]] = ensemble["plans"]

    N: int = int(metadata["D"])
    seed: int = starting_seed(args.state, N)

    # Instantiate a scorer

    scorer: Scorer = Scorer(
        data,
        shapes,
        graph,
        metadata,
        verbose=args.verbose,
    )

    # For each pair of ratings dimensions frontier

    pushed_plans: List[Dict[str, Name | Weight | Dict[GeoID, DistrictID]]] = []

    for i, frontier_key in enumerate(frontiers["frontiers"].keys()):
        if args.verbose:
            print()
            print(
                f">>> Pushing the {frontier_key} frontier point ({i+1} of {len(frontiers['frontiers'].keys())}) <<<"
            )

        plan_names: List[Dict[str, Any]] = frontiers["frontiers"][frontier_key]
        plan_names = ["test"]  # DEBUG

        for j, plan_name in enumerate(plan_names):
            # TODO - Use the plan_name to get the plan from the ensemble
            # DEBUG
            p: Dict[str, Name | Weight | Dict[GeoID, DistrictID]] = plans[0]
            name: Name = str(p["name"])
            district_by_geoid: Dict[GeoID, DistrictID] = p["plan"]  # type: ignore

            # Push each frontier point one or more times

            frontier_pair: List[str] = list(frontier_key.split("_"))
            dimensions: Tuple[str, str] = (frontier_pair[0], frontier_pair[1])

            for j in range(1, args.multiplier + 1):
                if args.verbose:
                    print()
                    print(f"Search {j} of {args.multiplier}")

                try:
                    plan: Plan = Plan(
                        district_by_geoid,
                        pop_by_geoid,
                        graph,
                        seed,
                        verbose=args.verbose,
                        # debug=args.debug,
                    )
                    beg_measures = scorer.measure_dimensions(
                        plan.to_assignments(), dimensions
                    )

                    # plan.to_csv("output/test_starting_plan.csv") # DEBUG

                    plan_name: str = f"{frontier_key}_{i:03d}"
                    assignments: Dict[GeoID, DistrictID] = push_point(
                        plan,
                        scorer,
                        dimensions,
                        verbose=args.verbose,
                        # debug=args.debug,
                    )
                    end_measures = scorer.measure_dimensions(
                        plan.to_assignments(), dimensions
                    )

                    # plan.to_csv(f"output/test_pushed_{frontier_key}_plan.csv") # DEBUG

                    if args.verbose:
                        print()
                        print(
                            f"Improved {dimensions} from {beg_measures} to {end_measures}."
                        )

                    pushed_plans.append(
                        {"name": plan_name, "plan": assignments}
                    )  # No weights.

                except:
                    pass
                finally:
                    seed += 1

        break  # DEBUG

    pushed_ensemble: Dict[str, Any] = ensemble_metadata(
        xx=args.state,
        ndistricts=N,
        size=len(pushed_plans),
        method="Maps pushed from the frontier points",
        repo="rdatools/tradeoffs",
    )
    pushed_ensemble["plans"] = pushed_plans

    write_json(args.pushed, pushed_ensemble)


if __name__ == "__main__":
    main()

### END ###
