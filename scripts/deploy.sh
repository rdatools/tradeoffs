#!/bin/bash
#
# Copy the artifacts for a state from fileout to docs
#
# For example:
#
# scripts/DEPLOY.sh NC

XX=$1
FROM_DIR=../../iCloud/fileout
TO_DIR=docs

cp $FROM_DIR/images/$XX*.svg $TO_DIR/assets/images
cp $FROM_DIR/_data/$XX*.csv $TO_DIR/_data
