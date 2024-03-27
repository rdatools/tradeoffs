#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Error: No input files provided." >&1
    exit 1
fi

head -n 1 "$1"

for file in "$@"; do
    tail -n +2 "$file"
done

