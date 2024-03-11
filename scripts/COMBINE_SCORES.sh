#!/bin/bash
#
# Combine the scores from the original ensemble and the pushed plans
#
# For example:
#
# scripts/COMBINE_SCORES.sh NC

XX=$1
WORKING_DIR=../../iCloud/fileout/ensembles

tail -n +2 $WORKING_DIR/${XX}20C_scores_pushed.csv > $WORKING_DIR/scores.tmp && mv $WORKING_DIR/scores.tmp $WORKING_DIR/${XX}20C_scores_pushed.csv
cat $WORKING_DIR/${XX}20C_scores.csv $WORKING_DIR/${XX}20C_scores_pushed.csv > $WORKING_DIR/${XX}20C_scores_augmented.csv
