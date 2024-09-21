#!/usr/bin/env python3

"""
GENERATE THE WORKFLOW FOR A STATE

For example:

$ scripts/make_states_yml.py 

For documentation, type:

$ scripts/make_states_yml.py -h
"""

from typing import Dict, List

from rdabase import (
    STATES,
    STATE_NAMES,
    DISTRICTS_BY_STATE,
    COUNTIES_BY_STATE,
    load_data,
    populations,
    total_population,
)

states_with_data: List[str] = [
    "AL",
    "AZ",
    "FL",
    "GA",
    "IL",
    "IN",
    "MD",
    "MI",
    "NC",
    "NJ",
    "NM",
    "OH",
    "PA",
    "SC",
    "TX",
    "VA",
    "WI",
]


def main() -> None:
    """Generate states.yml"""

    for xx in STATES:
        print(f"- xx: {xx}")
        print(f"  name: {STATE_NAMES[xx]}")
        for plan_type in ["congress", "upper", "lower"]:
            print(f"  {plan_type}: {DISTRICTS_BY_STATE[xx][plan_type]}")
        print(f"  counties: {COUNTIES_BY_STATE[xx]}")
        if xx in states_with_data:
            data_path: str = f"../rdabase/data/{xx}/{xx}_2020_data.csv"
            data: Dict[str, Dict[str, int | str]] = load_data(data_path)
            pop_by_geoid: Dict[str, int] = populations(data)
            total_pop: int = total_population(pop_by_geoid)
            print(f"  population: {total_pop}")
        else:
            print(f"  population: 0")


if __name__ == "__main__":
    main()

### END ###
