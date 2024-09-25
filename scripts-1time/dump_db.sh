#!/bin/bash
#
# Dump the published maps from the DRA database.
#
# For example:
#
# scripts/dump_db.sh
#

ROOT=~/dev/
SCRIPT_DIR=$ROOT\dra-cli

$SCRIPT_DIR/dumpdb.js -t state -x id accessMap xprops.state xprops.planType xprops.nDistricts xprops.score_complete xprops.score_contiguous xprops.score_freeofholes xprops.score_equalpopulation xprops.score_proportionality xprops.score_competitiveness xprops.score_minorityRights xprops.score_compactness xprops.score_splitting \
    -f published:true deleted:false \
    -p \
    > temp/published_maps.jsonl
