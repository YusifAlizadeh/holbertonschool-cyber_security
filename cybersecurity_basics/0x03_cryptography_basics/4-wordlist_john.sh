#!/bin/bash

# Check if a hash file was provided as an argument
if [ -z "$1" ]; then
    echo "Usage: $0 <hashfile>"
    exit 1
fi

HASH_FILE=$1
WORDLIST="/usr/share/wordlists/rockyou.txt"
OUTPUT_FILE="4-password.txt"

# 1. Run John the Ripper in Wordlist Mode
# --wordlist specifies the path to your dictionary
# --format can be added if you know the specific hash type (e.g., --format=raw-md5)
john --wordlist=$WORDLIST "$HASH_FILE"

# 2. Extract the cracked passwords from John's internal database
# The --show command displays the results in "hash:password" format
# We then redirect that output to your specified file
john --show "$HASH_FILE" > "$OUTPUT_FILE"

echo "-----------------------------------------------"
echo "Processing complete. Results saved to $OUTPUT_FILE"
