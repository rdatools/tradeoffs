#!/usr/bin/env python3

"""
DEBUGGING SCRIPT
"""

from typing import Any, List, Dict, NamedTuple

from rdabase import read_json
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


def main() -> None:
    args: Args = Args(
        state="NC",
        plans="testdata/synthetic_plans.json",
        frontier="testdata/synthetic_frontier.json",
        data="../rdabase/data/NC/NC_2020_data.csv",
        shapes="../rdabase/data/NC/NC_2020_shapes_simplified.json",
        graph="../rdabase/data/NC/NC_2020_graph.json",
    )

    # Load data

    data: Dict[str, Dict[GeoID, DistrictID]] = load_data(args.data)
    shapes: Dict[str, Any] = load_shapes(args.shapes)
    graph: Dict[GeoID, List[GeoID]] = load_graph(args.graph)
    metadata: Dict[str, Any] = load_metadata(args.state, args.data)

    ensemble: Dict[str, Any] = read_json(args.plans)
    plans: List[Dict[str, Name | Weight | Dict[GeoID, DistrictID]]] = ensemble["plans"]

    # Get the first plan, for debugging

    p: Dict[str, Name | Weight | Dict[GeoID, DistrictID]] = plans[0]
    name: Name = str(p["name"])
    district_by_geoid: Dict[GeoID, DistrictID] = p["plan"]  # type: ignore

    #

    ep: EPlan = EPlan(district_by_geoid, graph)

    # Check each border feature

    district_pairs = ep.district_adjacencies()
    for pair in district_pairs:
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

                if not ep.is_connected(proposed):
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
