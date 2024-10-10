#!/bin/bash
#
# Push a tree of jobs to the UA cluster
#
# For example:
#
# scripts/PUSH.sh NC

XX=$1
FROM_DIR=/Users/alecramsay/iCloud/fileout/tradeoffs
TO_DIR=alecr@filexfer.hpc.arizona.edu:./dropbox

exclude_docs="'$FROM_DIR/$XX/docs/*'" 
exclude_ensembles="'$FROM_DIR/$XX/ensembles/*'" 
exclude_pushed="'$FROM_DIR/$XX/pushed/*'"

rsync -avz $FROM_DIR/$XX/ $TO_DIR/$XX --exclude $exclude_docs --exclude $exclude_ensembles --exclude $exclude_pushed