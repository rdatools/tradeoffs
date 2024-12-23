#!/usr/bin/env python3

"""
Duplicate Notable maps.

For example:

$ scripts-1time/make_dup_notables_script.py

For documentation, type:

$ scripts-1time/make_dup_notables_script.py -h

"""

from rdabase import yyyy
from constants import NOTABLE_MAPS

group: str = "TRADEOFFS"
label: str = "PG-NOTABLE"


def make_command(xx: str, plan_type: str, dim: str, label: str, id: str) -> str:
    # scripts-1time/duplicate_map.sh NC Congress 2022 Official PG-OFFICIAL c62fa27b-1f4b-40ba-bcd7-9e2ca6f9df87
    return f"scripts-1time/duplicate_map.sh {xx} {plan_type} {yyyy} {dim} {label} {id}"


unknown: str = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"

print("#!/bin/bash")
print("# Duplicate notable maps in DRA.")
print("# Remember to start the DRA server before running these commands!")
for xx, plan_types in NOTABLE_MAPS.items():
    for plan_type, notable_maps in plan_types.items():
        if plan_type == "congress":
            continue  # already duplicated
        if xx in ["NC", "MD"]:
            continue  # already duplicated
        for dim, url_frag in notable_maps.items():
            if url_frag == unknown:
                continue

            log_file: str = (
                f"intermediate/{xx}_{yyyy}_{plan_type.capitalize()}_{dim.capitalize()}_duplicate.log"
            )
            command: str = (
                make_command(xx, plan_type.capitalize(), dim, label, url_frag)
                + f" > {log_file}"
            )
            print(command)

pass
