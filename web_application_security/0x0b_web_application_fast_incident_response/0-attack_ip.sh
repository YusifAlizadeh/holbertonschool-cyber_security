LOG_FILE="logs.txt"

# Check if file exists
if [[ ! -f "$LOG_FILE" ]]; then
    echo "File $LOG_FILE not found."
    exit 1
fi

# Pipeline to extract IP, count occurrences, sort by frequency, and pick the top one
awk '{print $1}' "$LOG_FILE" | sort | uniq -c | sort -nr | head -n 1
