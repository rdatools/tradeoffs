#!/usr/bin/env python3

"""
MAKE A DICTIONARY OF NOTABLE GUID TEMPLATES FOR EACH STATE & PLAN TYPE
"""

from rdabase import DISTRICTS_BY_STATE


def main() -> None:

    for xx in DISTRICTS_BY_STATE:
        print(f'"{xx}": {{')

        for plan_type, ndistricts in DISTRICTS_BY_STATE[xx].items():
            if ndistricts is not None and ndistricts > 1:
                print(f'"{plan_type}": {{')

                for dimension in [
                    "proportional",
                    "competitive",
                    "minority",
                    "compact",
                    "splitting",
                ]:
                    print(f'"{dimension}": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",')

                print(f"}},")

        print(f"}},")

    pass


if __name__ == "__main__":
    main()

### END ###
