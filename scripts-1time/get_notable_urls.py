#!/usr/bin/env python3

"""
MAKE A DICTIONARY OF NOTABLE GUID TEMPLATES FOR EACH STATE & PLAN TYPE

For example:

$ scripts-1time/get_notable_urls.py > temp/notable_maps.json

"""

from typing import Dict, Any

from rdabase import read_json
from constants import NOTABLE_MAPS  # TODO


def main() -> None:

    data: Dict[str, Any] = read_json("docs/leaderboards.json")

    for xx, plan_types_dimensions in data.items():
        print(f"{xx}")

        for plan_type, dimension_leaders in plan_types_dimensions.items():
            print(f"  {plan_type}")

            for dimension, leaders in dimension_leaders.items():
                if len(leaders) == 0:
                    print(
                        f"    Warning: {xx}/{plan_type}/{dimension} has no candidate notable maps!"
                    )
                    continue

                print(f"    {dimension}")

                best_map = leaders[0]["url"]
                print(f"      {best_map}")

    pass


if __name__ == "__main__":
    main()

### END ###
