#!/bin/bash
#
# Export a precinct-assignment file for a no-splits official proxy map from DRA, and
# rename it.
#
# For example:
#
# scripts-1time/export_official_proxy.sh --state NC --plantype upper --name NC_2022_Upper_Official_Proxy.csv
#

# Initialize variables
state=""
plantype=""
name=""

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --state)
            state="$2"
            shift 2
            ;;
        --plantype)
            plantype="$2"
            shift 2
            ;;
        --name)
            name="$2"
            shift 2
            ;;
        *)
            echo "Unknown parameter: $1"
            exit 1
            ;;
    esac
done

# Check if all required parameters are provided
if [[ -z $state || -z $plantype || -z $name ]]; then
    echo "Error: All parameters (--state, --plantype, --name) are required."
    echo "Usage: $0 --state <state> --plantype <plantype> --name <name>"
    exit 1
fi

echo scripts-1time/export_official_proxy.py --state $state --plantype $plantype --no-debug
scripts-1time/export_official_proxy.py --state $state --plantype $plantype --no-debug

echo mv ~/Downloads/precinct-assignments.csv ~/dev/rdaensemble/official_maps/$name
mv ~/Downloads/precinct-assignments.csv ~/dev/rdaensemble/official_maps/$name