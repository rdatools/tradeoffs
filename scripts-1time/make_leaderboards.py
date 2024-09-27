#!/usr/bin/env python3

"""
GET THE CURRENT BEST MAPS FOR EACH STATE & PLAN TYPE

For example:

$ scripts-1time/make_leaderboards.py > temp/leaderboards.json 

First, dump the published maps, using the following command:

$ scripts-1time/dump_db.sh

"""

from typing import List, Dict, NamedTuple

import json

import warnings

warnings.warn = lambda *args, **kwargs: None

from rdabase import DISTRICTS_BY_STATE
from rdaensemble import ratings_dimensions

from constants import NOTABLE_MAPS


class MapAbstract(NamedTuple):
    id: str
    url_fragment: str
    cycle: str
    xx: str
    plan_type: str
    nDistricts: int
    constraints: List[bool]
    ratings: List[int]
    total: int


def map_abstract(json_data: Dict) -> MapAbstract:
    """
    Convert the JSON object to a flat dict format.

    {
    "id": "9f9604cc-b74b-44d2-84d0-6838192820f9",
    "accessMap": {
    "a33097f7-7457-4a5c-ada8-7b1722fc5acf": {
    "perm": 3,
    "userIDs": []
    },
    "e0788f78-67e1-4918-bcf3-e3e51e32354b": {
    "perm": 1,
    "userIDs": []
    }
    },
    "datasource": "2010_VD",
    "state": "NE",
    "nDistricts": "3",
    "score_complete": "0",
    "score_contiguous": "0",
    "score_freeofholes": "0",
    "score_equalpopulation": "0",
    "score_proportionality": "66",
    "score_competitiveness": "51",
    "score_minorityRights": "0",
    "score_compactness": "71",
    "score_splitting": "95"
    }
    """

    required_keys = [
        "id",
        "accessMap",
        "datasource",
        "state",
        "planType",
        "nDistricts",
        "score_complete",
        "score_contiguous",
        "score_freeofholes",
        "score_equalpopulation",
        "score_proportionality",
        "score_competitiveness",
        "score_minorityRights",
        "score_compactness",
        "score_splitting",
    ]

    if not all(k in json_data for k in required_keys):
        raise ValueError(f"{json_data}")

    cycle: str = "2020" if json_data["datasource"] == "2020_VD" else "2010"
    id: str = json_data["id"]
    access_map: Dict = json_data["accessMap"]
    url_fragment: str = "N/A"
    for k, v in access_map.items():
        if v["perm"] == 1:
            url_fragment = k
            break

    xx: str = json_data["state"]
    plan_type: str = json_data["planType"]
    ndistricts: int = int(json_data["nDistricts"])

    is_complete: bool = True if int(json_data["score_complete"]) == 0 else False
    is_contiguous: bool = True if int(json_data["score_contiguous"]) == 0 else False
    is_free_of_holes: bool = True if int(json_data["score_freeofholes"]) == 0 else False
    is_roughly_equal: bool = (
        True if int(json_data["score_equalpopulation"]) == 0 else False
    )
    constraints: List[bool] = [
        is_complete,
        is_contiguous,
        is_free_of_holes,
        is_roughly_equal,
    ]
    ratings: List[int] = [int(json_data[k]) for k in required_keys[-5:]]

    abstract = MapAbstract(
        id=id,
        url_fragment=url_fragment,
        cycle=cycle,
        xx=xx,
        plan_type=plan_type,
        nDistricts=ndistricts,
        constraints=constraints,
        ratings=ratings,
        total=sum(ratings),
    )

    return abstract


def is_realistic(ratings: List[int]) -> bool:
    """
    Do a set of ratings meet DRA's 'realistic' thresholds?

    See 'Realistic' @ https://medium.com/dra-2020/notable-maps-66d744933a48
    """

    thresholds: List[int] = [20, 10, 0, 20, 20]

    return all(r >= t for r, t in zip(ratings, thresholds))


def is_conforming_map(ma: MapAbstract) -> bool:
    """Does a map abstract conform to the DRA notable maps 'realistic' criteria?"""

    if ma.cycle != "2020":
        return False

    if ma.xx not in DISTRICTS_BY_STATE:
        return False

    if ma.plan_type not in ["congress", "upper", "lower"]:
        return False

    if ma.nDistricts != DISTRICTS_BY_STATE[ma.xx][ma.plan_type] or ma.nDistricts <= 1:
        return False

    if not all(ma.constraints):
        return False

    if not is_realistic(ma.ratings):
        return False

    return True


def main() -> None:

    input_dir: str = "temp"
    output_dir: str = "temp"

    verbose: bool = False

    #
    maps_by_xx: Dict[str, Dict[str, List[MapAbstract]]] = {}
    for xx, plan_types_notables in NOTABLE_MAPS.items():
        maps_by_xx[xx] = {}

        for plan_type, _ in plan_types_notables.items():
            maps_by_xx[xx][plan_type] = []

    leaderboards: Dict[str, Dict[str, Dict[str, List[Dict[str, str]]]]] = {}
    leaders_by_dim: Dict[str, List[Dict[str, str]]] = {
        k: [] for k in ratings_dimensions
    }

    for xx, plan_types_notables in NOTABLE_MAPS.items():
        leaderboards[xx] = {}

        for plan_type, _ in plan_types_notables.items():
            leaderboards[xx][plan_type] = dict(leaders_by_dim)

    dump_path: str = f"{input_dir}/published_maps.json"

    # Find the conforming candidate maps

    with open(dump_path, "r") as f:
        lines: List[str] = f.readlines()

        record: str = ""
        total_maps: int = 0
        cycle_2020_maps: int = 0
        conforming_maps: int = 0

        for i, l in enumerate(lines):
            line: str = l.rstrip()

            if line == "":  # blank line between records
                json_data = json.loads(record)
                total_maps += 1

                try:
                    ma: MapAbstract = map_abstract(json_data)

                    if not ma.cycle == "2020":
                        record = ""
                        continue

                    cycle_2020_maps += 1

                    if not is_conforming_map(ma):
                        record = ""
                        continue

                    conforming_maps += 1

                    maps_by_xx[ma.xx][ma.plan_type].append(ma)

                except Exception as e:
                    if verbose:
                        print(f"Error processing map record: {e}")

                record = ""  # Start a new record
            record += line

    # print(f"# total maps: {total_maps}")
    # print(f"# 2020 maps: {cycle_2020_maps}")
    # print(f"# conforming maps: {conforming_maps}")

    # For each state, plan type, and ratings dimension, sort the maps by ratings and select the top 10

    for xx, plan_types in maps_by_xx.items():
        for plan_type, maps in plan_types.items():
            for i, dim in enumerate(ratings_dimensions):

                # Sort the map by highest to lowest ratings, breaking ties by the total ratings
                maps.sort(
                    key=lambda ma: (ma.ratings[i] + (ma.total / 1000)), reverse=True
                )

                leaders: List[Dict[str, str]] = [
                    {"id": ma.id, "url": ma.url_fragment} for ma in maps[:10]
                ]

                leaderboards[xx][plan_type][dim] = leaders

    # Convert the leaderboard to JSON and print it

    json_string = json.dumps(leaderboards, indent=2)
    print(json_string)

    pass


if __name__ == "__main__":
    main()

### END ###
