#!/usr/bin/env python3

"""
DEBUGGING SCRIPT
"""

from typing import Any, List, Dict, NamedTuple

from rdabase import read_json
from rdaensemble.general import ratings_dimensions, plan_from_ensemble, make_plan
from rdascore import load_data, load_shapes, load_graph, load_metadata

from tradeoffs import EvolvingPlan


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

    data: Dict[str, Dict[str, int | str]] = load_data(args.data)
    shapes: Dict[str, Any] = load_shapes(args.shapes)
    graph: Dict[str, List[str]] = load_graph(args.graph)
    metadata: Dict[str, Any] = load_metadata(args.state, args.data)

    ensemble: Dict[str, Any] = read_json(args.plans)
    plans: List[Dict[str, str | float | Dict[str, int | str]]] = ensemble["plans"]

    # Get the first plan, for debugging

    p: Dict[str, str | float | Dict[str, int | str]] = plans[0]
    name: str = str(p["name"])
    district_by_geoid: Dict[str, int | str] = p["plan"]  # type: ignore

    #

    ep: EvolvingPlan = EvolvingPlan(district_by_geoid, graph)
    district_pairs = ep.district_adjacencies()

    # ep.to_csv("output/test_plan.csv")

    pass


if __name__ == "__main__":
    main()

### END ###
