#!/bin/bash
#
# Copy the artifacts for a state from fileout to the docs/ subdirectory.
# Note - This copies *all* the artifacts for a state (congress, upper, & lower).
#
# For example:
#
# scripts/DEPLOY.sh NC

XX=$1

FROM_DIR=../../temp/tradeoffs/${XX}
TO_DIR=docs

cp $FROM_DIR/docs/assets/images/*.svg $TO_DIR/assets/images
cp $FROM_DIR/docs/_data/*.csv $TO_DIR/_data
