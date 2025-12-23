#!/bin/bash

# Show the last 5 login sessions with date and time
# Must be run as root or with sudo

if [[ $EUID -ne 0 ]]; then
    echo "Please run this script as root or using sudo."
    exit 1
fi

last -n 5
