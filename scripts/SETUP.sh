#!/bin/bash
#
# Create the directories in fileout for a state
#
# For example:
#
# scripts/SETUP.sh NC

XX=$1
ROOT_DIR=../../iCloud/fileout/tradeoffs

mkdir $ROOT_DIR/$XX
# mkdir $ROOT_DIR/$XX/data
mkdir $ROOT_DIR/$XX/docs
mkdir $ROOT_DIR/$XX/ensembles
# mkdir $ROOT_DIR/$XX/plans
# mkdir $ROOT_DIR/$XX/jobs
# mkdir $ROOT_DIR/$XX/pushed

mkdir $ROOT_DIR/$XX/docs/_data
mkdir $ROOT_DIR/$XX/docs/assets
mkdir $ROOT_DIR/$XX/docs/assets/images