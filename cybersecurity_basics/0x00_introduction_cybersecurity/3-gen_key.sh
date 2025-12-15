#!/bin/bash
if [ -z "$1" ]; then
  echo "Usage: $0 <key_name>"
  exit 1
fi

KEY_NAME="$1"

# Generate RSA 4096-bit SSH key using OpenSSH
ssh-keygen -t rsa -b 4096 -f "$KEY_NAME"
