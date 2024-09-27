#!/usr/bin/env python3

"""
MAKE A DICTIONARY OF OFFICIAL GUIDS FOR EACH STATE & PLAN TYPE
"""

from typing import Any, List, Dict

from rdabase import STUDY_STATES, read_json


def main() -> None:

    data: Dict[str, Any] = read_json("scripts-1time/state_plans.json")

    for xx in STUDY_STATES:  # States w/ 2 or more congressional districts
        if xx not in data:
            continue

        print(f'"{xx}": {{')
        plans: List[Dict[str, Any]] = data[xx]["plans"]
        latest: List[Dict[str, Any]] = [p for p in plans if p["year"] == 2022]
        for i, plan in enumerate(latest):
            trailing_comma = "," if i < len(latest) - 1 else ""
            print(f'"{plan["planType"]}": "{plan["id"]}"{trailing_comma}')
        print(f"}},")

    pass


if __name__ == "__main__":
    main()

### END ###
