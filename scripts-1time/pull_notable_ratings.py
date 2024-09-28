#!/usr/bin/env python3
#

"""
Generate a shell script to pull the ratings for copies of notable maps in DRA.

For example:

$ scripts-1time/pull_notable_ratings.py

For documentation, type:

$ scripts-1time/pull_notable_ratings.py -h

"""

from rdabase import plan_type, yyyy
from constants import NOTABLE_MAPS_COPY

output_dir: str = "intermediate"

print("#!/bin/bash")
print("# Pull ratings for copies of notable maps in DRA.")
for xx, plan_type_url_frags in NOTABLE_MAPS_COPY.items():
    for plan_type, notable_maps in plan_type_url_frags.items():
        if plan_type == "congress":
            continue  # already duplicated

        for dim, url_frag in notable_maps.items():
            if url_frag == "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx":
                continue
            command: str = (
                f"scripts-1time/pull_map_ratings.sh {xx} {yyyy} {plan_type.capitalize()} {dim.capitalize()} {url_frag} {output_dir}"
            )
            print(command)
            # os.system(command)

pass


### END ###
