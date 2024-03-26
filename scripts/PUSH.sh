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

rsync -avz $FROM_DIR/$XX/data $TO_DIR/$XX
rsync -avz $FROM_DIR/$XX/jobs $TO_DIR/$XX
rsync -avz $FROM_DIR/$XX/plans $TO_DIR/$XX
cp $FROM_DIR/$XX/*.sh $TO_DIR/$XX