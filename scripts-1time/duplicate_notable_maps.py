#!/usr/bin/env python3

"""
Duplicate Notable maps.

For example:

$ scripts-1time/duplicate_notable_maps.py

For documentation, type:

$ scripts-1time/duplicate_notable_maps.py -h

"""

from rdabase import plan_type, yyyy
from constants import NOTABLE_MAPS

group: str = "Notable"
label: str = "PG-" + group.upper()


def make_command(group: str, label: str, xx: str, id: str) -> str:
    # scripts-1time/duplicate_map.sh NC Congress 2022 Proportional PG-NOTABLE 7cfcec86-b8bf-41fa-a6c2-0be9b3799747
    return (
        f"scripts-1time/duplicate_map.sh {xx} {plan_type} {yyyy} {group} {label} {id}"
    )


print("#!/bin/bash")
print("# Duplicate notable maps in DRA.")
for xx, plan_types in NOTABLE_MAPS.items():
    for plan_type, notable_maps in plan_types.items():
        if plan_type == "congress":
            continue  # already duplicated
        if xx in ["NC", "MD"]:
            continue  # already duplicated
        for dim, guid in notable_maps.items():
            print(make_command(dim.capitalize(), label, xx, guid))
            #  os.system(make_command(dim.capitalize(), label, xx, id))

pass
