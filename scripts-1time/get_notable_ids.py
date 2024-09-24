#!/usr/bin/env python3

"""
GET IDS FOR EACH NOTABLE MAP FOR EACH STATE & PLAN TYPE

First, dump the published maps:

$ dumpdb.js -t state -x id accessMap xprops.state xprops.planType xprops.nDistricts xprops.score_complete xprops.score_contiguous xprops.score_freeofholes xprops.score_equalpopulation xprops.score_proportionality xprops.score_competitiveness xprops.score_minorityRights xprops.score_compactness xprops.score_splitting \
    -f published:true deleted:false \
    -p \
    > temp/published_maps.json

"""

from rdabase import DISTRICTS_BY_STATE


def main() -> None:

    # TODO - Everything below this line is a placeholder

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
