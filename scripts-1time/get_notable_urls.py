#!/usr/bin/env python3

"""
MAKE A DICTIONARY OF NOTABLE GUID TEMPLATES FOR EACH STATE & PLAN TYPE

For example:

$ scripts-1time/get_notable_urls.py > temp/notable_maps.json

"""

from typing import List, Dict, Any

import json

from rdabase import read_json
from constants import OFFICIAL_MAPS_COPY, NOTABLE_MAPS


def main() -> None:

    data: Dict[str, Any] = read_json("docs/leaderboards.json")
    no_leaders: List[Dict[str, str]] = []
    unknown: str = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"

    for xx, plan_types_dimensions in data.items():
        # print(f"{xx}")

        for plan_type, dimension_leaders in plan_types_dimensions.items():
            # print(f"  {plan_type}")

            for dimension, leaders in dimension_leaders.items():
                # print(f"    {dimension}")
                best_map: str = ""

                if len(leaders) == 0:
                    best_map = unknown
                    if xx in OFFICIAL_MAPS_COPY:
                        no_leaders.append(
                            {"xx": xx, "plan_type": plan_type, "dimension": dimension}
                        )
                        official_url_frag: str = OFFICIAL_MAPS_COPY[xx][plan_type]
                        best_map = official_url_frag
                else:
                    best_map = leaders[0]["url"]

                # print(f"      {best_map}")

                if xx in NOTABLE_MAPS and plan_type in NOTABLE_MAPS[xx]:
                    NOTABLE_MAPS[xx][plan_type][dimension] = best_map

    json_string = json.dumps(NOTABLE_MAPS, indent=2)
    print(json_string)

    # print("\n\n\n")
    # print("State / plan type / dimension combos with no leaders:")
    # for combo in no_leaders:
    #     print(combo)

    pass


if __name__ == "__main__":
    main()

### END ###
