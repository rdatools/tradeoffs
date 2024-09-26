#!/usr/bin/env python3

"""
GET NOTABLE MAP CANDIDATES FOR EACH STATE & PLAN TYPE
AS WELL AS THE CURRENT BEST MAPS

First, dump the published maps, using the following command:

$ scripts-1time/dump_db.sh

"""

from typing import List, Dict, Optional

import json

from rdabase import read_json, STATES, DISTRICTS_BY_STATE

from constants import NOTABLE_MAPS


def main() -> None:

    input_dir: str = "temp"
    output_dir: str = "temp"

    #

    leaderboards: Dict[str, Dict[str, Dict[str, List[Dict]]]] = {}
    unknowns: Dict[str, List] = {
        "proportional": [],
        "competitive": [],
        "minority": [],
        "compact": [],
        "splitting": [],
    }

    for xx, plan_types_notables in NOTABLE_MAPS.items():
        leaderboards[xx] = {}

        for plan_type, dim_id in plan_types_notables.items():
            for dim, _ in dim_id.items():
                leaderboards[xx][plan_type] = dict(unknowns)

    dump_path: str = f"{input_dir}/published_maps.json"

    with open(dump_path, "r") as f:
        lines: List[str] = f.readlines()
        print(f"# of input lines: {len(lines)}")

        record: str = ""
        total_maps: int = 0
        conforming_maps: int = 0

        for i, l in enumerate(lines):
            line: str = l.rstrip()
            # print(f"line {i}: {line}")

            if line == "":  # blank line between records
                json_data = json.loads(record)
                total_maps += 1

                """
                Convert the JSON object to a flat dict format.

                {
                    "id": "c491cfd1-e14c-4a7b-9d49-0238528a596a",
                    "accessMap": {
                    "a980332d-bd33-42ed-a5dd-7ec88d7907e8": {
                    "perm": 3,
                    "userIDs": []
                    },
                    "6539f6ad-5ea1-4a50-846b-27a1f1201f83": {
                    "perm": 1,
                    "userIDs": []
                    }
                    },
                    "state": "PA",
                    "planType": "congress",
                    "nDistricts": "17",
                    "score_complete": "0",
                    "score_contiguous": "0",
                    "score_freeofholes": "0",
                    "score_equalpopulation": "1",
                    "score_proportionality": "0",
                    "score_competitiveness": "40",
                    "score_minorityRights": "49",
                    "score_compactness": "65",
                    "score_splitting": "63"
                    }
             
                """
                required_keys = [
                    "state",
                    "planType",
                    "nDistricts",
                    "score_complete",
                    "score_contiguous",
                    "score_freeofholes",
                    "score_equalpopulation",
                ]
                if not all(k in json_data for k in required_keys):
                    print(f"Skipping incomplete record #{total_maps}.")
                    record = ""
                    continue

                xx: str = json_data["state"]
                plan_type: str = json_data["planType"]
                ndistricts: int = int(json_data["nDistricts"])
                is_complete: bool = (
                    True if int(json_data["score_complete"]) == 0 else False
                )
                is_contiguous: bool = (
                    True if int(json_data["score_contiguous"]) == 0 else False
                )
                is_free_of_holes: bool = (
                    True if int(json_data["score_freeofholes"]) == 0 else False
                )
                is_roughly_equal: bool = (
                    True if int(json_data["score_equalpopulation"]) == 0 else False
                )
                # TODO - More ...

                if (
                    (xx is None)
                    or (xx not in DISTRICTS_BY_STATE)
                    or (
                        plan_type is None
                        or plan_type not in ["congress", "upper", "lower"]
                    )
                    or (
                        ndistricts is None
                        or ndistricts != DISTRICTS_BY_STATE[xx][plan_type]
                        or ndistricts <= 1
                    )
                    or (
                        not is_complete
                        or not is_contiguous
                        or not is_free_of_holes
                        or not is_roughly_equal
                    )
                ):
                    print("Skipping 'unrealistic' record #{total_maps}.")
                    record = ""
                    continue  # Skip this record

                conforming_maps += 1
                print("Keeping record {total_maps}.")
                print(
                    f"Record #{total_maps}: {xx}/{plan_type} n: {ndistricts}, complete: {is_complete}, contiguous: {is_contiguous}, free of holes: {is_free_of_holes}, roughly equal: {is_roughly_equal}"
                )

                # TODO - Finish building the abstract

                record = ""  # Start a new record
            record += line

    print(f"# total maps: {total_maps}")
    print(f"# conforming maps: {conforming_maps}")

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
