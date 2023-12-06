#!/bin/bash

# Check if the required number of arguments are provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <file_to_check> <reference_file>"
    exit 1
fi

file_to_check="$1"
reference_file="$2"

# Loop through each line in the file_to_check
while IFS= read -r line; do
    # Use grep to check if the line exists in the reference_file
    if ! grep -qF "$line" "$reference_file"; then
        echo "Error: Line not found in reference file: $line"
    fi
    echo "finding"
done < "$file_to_check"

echo "All lines from $file_to_check are included in $reference_file"
