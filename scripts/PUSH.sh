#!/bin/bash
#
# Push a tree of jobs to the UA cluster
#
# For example:
#
# scripts/SETUP.sh NC

XX=$1
FROM_DIR=/Users/alecramsay/iCloud/fileout/tradeoffs
TO_DIR=alecr@filexfer.hpc.arizona.edu:./dropbox

rsync -avz $FROM_DIR/$XX/ $TO_DIR/$XX