#!/bin/bash

# Define log file
LOG_FILE="logs.txt"

# Check if file exists
if [[ ! -f "$LOG_FILE" ]]; then
    echo "File $LOG_FILE not found."
    exit 1
fi

# Extract IPs, count them, sort by most frequent, and display the top result
awk '{print $1}' "$LOG_FILE" | sort | uniq -c | sort -nr | head -n 1
