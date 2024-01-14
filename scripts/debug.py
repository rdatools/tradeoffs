#!/usr/bin/env python3

"""
DEBUGGING SCRIPT
"""

from typing import Any, List, Dict, NamedTuple

from rdabase import read_json, starting_seed
from rdaensemble.general import ratings_dimensions, plan_from_ensemble, make_plan
from rdascore import load_data, load_shapes, load_graph, load_metadata

from tradeoffs import *  # TODO


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

    ## Get a plan and ratings for debugging ##

    frontier: List[Dict[str, Any]] = frontiers["frontiers"][
        "proportionality_compactness"
    ]
    # ratings: List[int] = frontier[0]["ratings"]

    # Use the offset in the frontier, to get the plan in the ensemble

    p: Dict[str, Name | Weight | Dict[GeoID, DistrictID]] = plans[0]
    name: Name = str(p["name"])
    district_by_geoid: Dict[GeoID, DistrictID] = p["plan"]  # type: ignore

    ##

    ep: EPlan = EPlan(
        district_by_geoid, pop_by_geoid, graph, seed, verbose=args.verbose
    )
    # print(ep)

    # Check each border feature

    random_districts = ep.random_districts()
    for pair in random_districts:
        print(f"Adjacent: {pair}")

        for i, _ in enumerate(pair):
            j: Offset = (i + 1) % 2

            d1: DistrictID = pair[i]
            d2: DistrictID = pair[j]

            print(f"... DistrictID {d1}:")

            features: List[Offset] = list(ep.district_features(d1))
            border_features: Set[Offset] = ep.border_features(d1, d2)

            for candidate in border_features:
                proposed: List[Offset] = features.copy()
                proposed.remove(candidate)

                if not ep._is_connected(proposed):
                    print(
                        f"...... DistrictID would not be connected, if feature {candidate} were removed!"
                    )
                else:
                    print(
                        f"...... DistrictID would be connected, if feature {candidate} were removed."
                    )

    # ep.to_csv("output/test_plan.csv")

    pass


if __name__ == "__main__":
    main()

### END ###
