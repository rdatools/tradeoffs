#!/usr/bin/env python3

"""
GET NOTABLE MAP CANDIDATES FOR EACH STATE & PLAN TYPE
AS WELL AS THE CURRENT BEST MAPS

First, dump the published maps, using the following command:

$ scripts-1time/dump_db.sh

"""

from typing import List, Dict

import json

from rdabase import read_json, DISTRICTS_BY_STATE


def main() -> None:

    input_dir: str = "temp"
    output_dir: str = "temp"

    dump_path: str = f"{input_dir}/published_maps.json"

    with open(dump_path, "r") as f:
        lines: List[str] = f.readlines()
        maps_jsons: List[Dict] = []

        record: str = ""
        for l in lines:
            line: str = l.rstrip()
            if line == "":
                json_data = json.loads(record)
                maps_jsons.append(json_data)
                record = ""
            record += line

        pass

    # for xx in DISTRICTS_BY_STATE:
    #     print(f'"{xx}": {{')

    #     for plan_type, ndistricts in DISTRICTS_BY_STATE[xx].items():
    #         if ndistricts is not None and ndistricts > 1:
    #             print(f'"{plan_type}": {{')

    #             for dimension in [
    #                 "proportional",
    #                 "competitive",
    #                 "minority",
    #                 "compact",
    #                 "splitting",
    #             ]:
    #                 print(f'"{dimension}": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",')

    #             print(f"}},")

    #     print(f"}},")

    pass


if __name__ == "__main__":
    main()

### END ###
