#!/bin/bash
#
# Create the directories in fileout for a state
#
# For example:
#
# scripts/SETUP.sh NC

XX=$1
ROOT_DIR=../../iCloud/fileout/hpc_dropbox

mkdir $ROOT_DIR/$XX
mkdir $ROOT_DIR/$XX/data
mkdir $ROOT_DIR/$XX/plans
mkdir $ROOT_DIR/$XX/jobs
mkdir $ROOT_DIR/$XX/pushed