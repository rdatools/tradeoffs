#!/usr/bin/env python3

"""
Gather the URL fragments of duplicated notable maps and create a dict structure for downstream use.
Paste the results into the NOTABLE_MAPS_COPY constant in constants.py.

For example:

$ scripts-1time/get_duplicated_notable_map_urls.py

For documentation, type:

$ scripts-1time/get_duplicated_notable_map_urls.py -h

"""

from typing import List

import os

from rdabase import yyyy
from constants import NOTABLE_MAPS

input_dir: str = "intermediate"
unknown_url: str = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"


def url_from_duplicate_log(log_path: str) -> str:
    """Extract the url from the 'duplicate' command log output.

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
        url: str = lines[4].split(" ")[5].rstrip()

        return url


print()
print(f"NOTABLE_MAPS_COPY: Dict[str, Dict[str, str]] = {{")
for xx, plan_type_dim_urls in NOTABLE_MAPS.items():
    print(f'"{xx}": {{')

    for plan_type, plan_dim_urls in plan_type_dim_urls.items():
        print(f'"{plan_type}": {{')

        for dim, url in plan_dim_urls.items():
            url = unknown_url
            if plan_type == "congress":
                print(f'"{dim}": "{unknown_url}",')
            else:
                log_path: str = (
                    f"{input_dir}/{xx}_{yyyy}_{plan_type.capitalize()}_{dim.capitalize()}_duplicate.log"
                )
                if os.path.exists(log_path):
                    url: str = url_from_duplicate_log(log_path)
                print(f'"{dim}": "{url}",')
        print(f"}},")
    print(f"}},")
print(f"}}")

pass

#
