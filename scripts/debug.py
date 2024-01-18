#!/usr/bin/env python3

"""
DEBUGGING SCRIPT
"""

from typing import Any, List, Dict, NamedTuple

import itertools

from rdabase import read_json, starting_seed
from rdaensemble.general import ratings_dimensions, plan_from_ensemble, make_plan
from rdascore import load_data, load_shapes, load_graph, load_metadata

from tradeoffs import Scorer


class Args(NamedTuple):
    state: str
    plans: str
    frontier: str
    data: str
    shapes: str
    graph: str
    verbose: bool


def main() -> None:
    args: Args = Args(
        state="NC",
        plans="testdata/synthetic_plans.json",
        frontier="testdata/synthetic_frontier.json",
        data="../rdabase/data/NC/NC_2020_data.csv",
        shapes="../rdabase/data/NC/NC_2020_shapes_simplified.json",
        graph="../rdabase/data/NC/NC_2020_graph.json",
        verbose=True,
    )

    # Load data

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

    # Instantiate a Scorer

    s: Scorer = Scorer(
        data,
        shapes,
        graph,
        metadata,
        verbose=args.verbose,
    )

    pairs: List[Tuple[str, str]] = list(itertools.combinations(ratings_dimensions, 2))
    for pair in pairs:
        frontier_key: str = "_".join(pair)
        points: List[Dict[str, Any]] = frontiers["frontiers"][frontier_key]
        # TODO - For each point in the frontier ...
        # TODO - Use the offset in the frontier to get the plan from the ensemble
        # HACK - Get a plan and ratings for debugging

        p: Dict[str, Name | Weight | Dict[GeoID, DistrictID]] = plans[0]
        name: Name = str(p["name"])
        district_by_geoid: Dict[GeoID, DistrictID] = p["plan"]  # type: ignore
        assignments: List[Assignment] = make_plan(district_by_geoid)

        # TODO - Evaluate the plan

        measurements: Tuple[float, float] = s.measure_dimensions(assignments, pair)

    pass


if __name__ == "__main__":
    main()

### END ###
