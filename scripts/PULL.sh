#!/bin/bash
#
# Pull a director of pushed plans from the UA cluster
#
# For example:
#
# scripts/SETUP.sh NC

XX=$1
FROM_DIR=alecr@filexfer.hpc.arizona.edu:./dropbox
TO_DIR=/Users/alecramsay/iCloud/fileout/hpc_dropbox

rsync -avz $FROM_DIR/$XX/pushed $TO_DIR/$XX