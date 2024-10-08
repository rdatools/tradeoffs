#!/usr/bin/env python3

"""
Create a shell script to duplicate Official maps in DRA,
so that no-split proxies can be created.

For example:

$ scripts-1time/make_dup_official_proxies_script.py

Remember to start a server. Open a new Terminal and type:

$ cd dra
$ npm run test

Then open a browser and go to http://localhost:3000/.

For documentation, type:

$ scripts-1time/make_dup_official_proxies_script.py -h

"""

from rdabase import yyyy
from constants import OFFICIAL_MAPS, TRADEOFFS_STATES

dim: str = "Official-Proxy"
label: str = "PG-OFFICIAL"


def make_command(xx: str, plan_type: str, dim: str, label: str, id: str) -> str:
    # scripts-1time/duplicate_map.sh NC Congress 2022 Official PG-OFFICIAL c62fa27b-1f4b-40ba-bcd7-9e2ca6f9df87
    return f"scripts-1time/duplicate_map.sh {xx} {plan_type} {yyyy} {dim} {label} {id}"


print("#!/bin/bash")
print("# Duplicate Official maps in DRA.")
print("# Remember to start the DRA server before running these commands!")
for xx, plan_type_ids in OFFICIAL_MAPS.items():
    if xx not in TRADEOFFS_STATES:
        continue

    for plan_type, guid in plan_type_ids.items():
        command: str = make_command(xx, plan_type.capitalize(), dim, label, guid)
        print(command)

pass

#
