#!/usr/bin/env python3

"""
DEBUGGING SCRIPT
"""

from typing import Any, List, Dict

from rdabase import read_json

# from rdaensemble.general import ratings_dimensions, plan_from_ensemble, make_plan
# from rdascore import load_data, load_shapes, load_graph, load_metadata


def main() -> None:
    args: Dict = {
        "state": "NC",
        "plans": "testdata/synthetic_plans.json",
        "frontier": "testdata/synthetic_frontier.json",
        "data": "../rdabase/data/NC/NC_2020_data.csv",
        "shapes": "../rdabase/data/NC/NC_2020_shapes_simplified.json",
        "graph": "../rdabase/data/NC/NC_2020_graph.json",
    }

    #

    ensemble: Dict[str, Any] = read_json(args["plans"])
    plans: List[Dict[str, str | float | Dict[str, int | str]]] = ensemble["plans"]

    #

    p: Dict[str, str | float | Dict[str, int | str]] = plans[0]
    name: str = str(p["name"])
    district_by_geoid: Dict[str, int | str] = p["plan"]  # type: ignore

    #

    pass


if __name__ == "__main__":
    main()

### END ###
