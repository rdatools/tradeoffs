#!/usr/bin/env python3
#

"""
Generate a shell script to make notable ratings tables for the copies of notable maps in DRA.

For example:

$ scripts-1time/make_notable_ratings_tables.py

For documentation, type:

$ scripts-1time/make_notable_ratings_tables.py -h

"""

from rdabase import plan_type, yyyy
from constants import NOTABLE_MAPS  # TODO - NOTABLE_MAPS_COPY

output_dir: str = "intermediate"

print("#!/bin/bash")
print("# Make notable ratings tables for the copies of notable maps in DRA.")
for xx, plan_type_ids in NOTABLE_MAPS.items():
    for plan_type, _ in plan_type_ids.items():
        if plan_type == "congress":
            continue  # already duplicated

        command: str = (
            f"scripts-1time/make_notable_ratings_table.py --state {xx} --plantype {plan_type.capitalize()}"
        )
        print(command)
        # os.system(command)

pass


### END ###
