#!/bin/bash
#
# Duplicate a map
#
# For example:
#
# scripts/duplicate_map.sh NC Congress 2022 Official PG-OFFICIAL c62fa27b-1f4b-40ba-bcd7-9e2ca6f9df87
# scripts/duplicate_map.sh NC Congress 2022 Proportional PG-NOTABLE 7cfcec86-b8bf-41fa-a6c2-0be9b3799747
#
# The 'id' for the "Trade-offs" groups is "5004e36d-c772-4bcc-a296-7ea27ab766c6".
# dumpdb.js -t groups | grep Trade-offs
#

XX=$1
PLAN_TYPE=$2
YYYY=$3
DIM=$4
LABEL=$5
ID=$6

ROOT=~/dev/
SCRIPT_DIR=$ROOT\dra-cli

USER=alec@davesredistricting.org
PW=mumble # TODO - change this to the real password

NAME="$XX $YYYY $PLAN_TYPE - $DIM"
DESC="Copy of $XX $DIM"

echo $SCRIPT_DIR/draclient.js -u $USER -x $PW -i $ID -d -N "$NAME" -D "$DESC" -L $LABEL TRADEOFFS -G 5004e36d-c772-4bcc-a296-7ea27ab766c6
$SCRIPT_DIR/draclient.js  -u $USER -x $PW -i $ID -d -N "$NAME" -D "$DESC" -L $LABEL TRADEOFFS -G 5004e36d-c772-4bcc-a296-7ea27ab766c6

