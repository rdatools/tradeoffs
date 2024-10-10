#!/bin/bash

# Default values
STATE=""
PLAN_TYPE=""
ROUGHLY_EQUAL=""

# Function to print usage
usage() {
    echo "Usage: $0 --state <STATE> --plan-type <PLAN_TYPE>"
    echo "  --state     : State abbreviation (e.g., NC)"
    echo "  --plan-type : Plan type (e.g., congress, upper, lower)"
    exit 1
}

# Parse command line arguments
while [[ "$#" -gt 0 ]]; do
    case $1 in
        --state) STATE="$2"; shift ;;
        --plan-type) PLAN_TYPE="$2"; shift ;;
        *) echo "Unknown parameter: $1"; usage ;;
    esac
    shift
done

# Check if all required parameters are provided
if [ -z "$STATE" ] || [ -z "$PLAN_TYPE" ]; then
    echo "Error: Missing required parameters."
    usage
fi

# Derive additional values

ENSEMBLES_DIR="ensembles-${PLAN_TYPE}"
if [ "$PLAN_TYPE" = "congress" ]; then
    ENSEMBLES_DIR="ensembles"
fi

LETTER="${PLAN_TYPE:0:1}"
SUFFIX=`echo "${LETTER}" | tr '[a-z]' '[A-Z]'`
PREFIX="${STATE}20${SUFFIX}"

ROUGHLY_EQUAL=0.01
ROUGHLY_EQUAL_HALF=0.01
if [ "$PLAN_TYPE" = "upper" ] || [ "$PLAN_TYPE" = "lower" ]; then
    ROUGHLY_EQUAL=0.10
    ROUGHLY_EQUAL_HALF=0.05
fi

# Echo parameters

echo
echo "STATE: $STATE"
echo "PLAN_TYPE: $PLAN_TYPE"
echo
echo "ENSEMBLES_DIR: $ENSEMBLES_DIR"
echo "PREFIX: $PREFIX"
echo "ROUGHLY_EQUAL: $ROUGHLY_EQUAL"
echo "ROUGHLY_EQUAL_HALF: $ROUGHLY_EQUAL_HALF"
echo
