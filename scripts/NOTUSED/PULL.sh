#!/bin/bash
#
# Pull a directory of pushed plans from the UA cluster
#
# For example:
#
# scripts/PULL.sh NC

XX=$1
FROM_DIR=alecr@filexfer.hpc.arizona.edu:./dropbox
TO_DIR=/Users/alecramsay/iCloud/fileout/tradeoffs

rsync -avz $FROM_DIR/$XX/pushed $TO_DIR/$XX