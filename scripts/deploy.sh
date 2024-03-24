#!/bin/bash
#
# Copy the artifacts for a state from fileout to docs
#
# For example:
#
# scripts/DEPLOY.sh NC

XX=$1
FROM_DIR=../../iCloud/fileout/tradeoffs/${XX}
TO_DIR=docs

mv $FROM_DIR/docs/assets/images/*.csv $FROM_DIR/docs/_data

cp $FROM_DIR/docs/assets/images/*.svg $TO_DIR/assets/images
cp $FROM_DIR/docs/_data/*.csv $TO_DIR/_data
