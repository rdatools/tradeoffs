#!/usr/bin/env python3

"""
Gather the ids of duplicated official maps and create a dict structure for downstream use.

For example:

$ scripts-1time/get_duplicated_official_map_ids.py

For documentation, type:

$ scripts-1time/get_duplicated_official_map_ids.py -h

"""

from typing import List

import os

from rdabase import yyyy
from constants import OFFICIAL_MAPS

input_dir: str = "intermediate"
unknown_id: str = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"


def id_from_duplicate_log(log_path: str) -> str:
    """Extract the id from the 'duplicate' command log output.

    Example log output:

    /Users/alecramsay/dev/dra-cli/draclient.js -u alec@davesredistricting.org -x Front.Seat -i 9b5ec272-1fba-4a7a-ac6c-f2dcb4c6d0ae -d -N CO 2022 Upper - Official -D Copy of CO Official -L PG-OFFICIAL TRADEOFFS -G 5004e36d-c772-4bcc-a296-7ea27ab766c6
    0: info: PATH: /login; STATUS: 200: RESULT: 0
    1: info: PATH: /api/sessions/userview; STATUS: 200: RESULT: 0
    2: info: PATH: /api/sessions/duplicate/9b5ec272-1fba-4a7a-ac6c-f2dcb4c6d0ae; STATUS: 200: RESULT: 0
    3: info: setting session to e89181c3-998a-41c0-8c73-735ff6b3f9cd
    4: info: PATH: /api/sessions/connect/e89181c3-998a-41c0-8c73-735ff6b3f9cd; STATUS: 200: RESULT: 0
    5: info: PATH: /api/sessions/update/e89181c3-998a-41c0-8c73-735ff6b3f9cd; STATUS: 200: RESULT: 0
    6: info: PATH: /api/sessions/groups; STATUS: 200: RESULT: 0
    7: info: SUMMARY: 6 total requests.
    8: info: SUMMARY: 0 total request retries.
    9: info: SUMMARY: 0 total forced errors seen.
    10: info: SUMMARY: 0 total failed requests.
    11: info: SUMMARY: 0 total requests with nonzero result.

    """

    with open(log_path, "r") as f:
        lines: List[str] = f.readlines()
        # The 6th token in line number 3.
        id: str = lines[4].split(" ")[5]

        return id


print()
print(f"OFFICIAL_MAPS: Dict[str, Dict[str, str]] = {{")
for xx, guids in OFFICIAL_MAPS.items():
    print(f'    "{xx}": {{')
    for plan_type, guid in guids.items():
        id = unknown_id
        if plan_type == "congress":
            print(f'        "{plan_type}": "{unknown_id}",')
        else:
            log_path: str = (
                f"{input_dir}/{xx}_{yyyy}_{plan_type.capitalize()}_duplicate.log"
            )
            if os.path.exists(log_path):
                id: str = id_from_duplicate_log(log_path)
            print(f'        "{plan_type}": "{id}",')
    print(f"    }},")
print(f"}}")

pass

#
