#!/bin/bash

# Define variables
HASH_FILE=$1
WORDLIST="/usr/share/wordlists/rockyou.txt"
OUTPUT_FILE="4-password.txt"

# 1. Run John the Ripper (Quiet mode to reduce terminal noise)
# We use --format=raw-md5 as these appear to be MD5 hashes
john --wordlist="$WORDLIST" --format=raw-md5 "$HASH_FILE" > /dev/null 2>&1

# 2. Extract ONLY the cracked passwords
# --show displays "hash:password". 'cut' grabs the second field.
# The 'grep' ensures we only get lines that actually contain a colon.
john --show --format=raw-md5 "$HASH_FILE" | grep ":" | cut -d: -f2 > "$OUTPUT_FILE"

# 3. Clean up: Remove the last line if it's the John summary (e.g., "3 passwords cracked")
# This ensures the line count matches the number of hashes
sed -i '$d' "$OUTPUT_FILE"
