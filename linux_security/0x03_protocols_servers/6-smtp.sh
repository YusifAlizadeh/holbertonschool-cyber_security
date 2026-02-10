#!/bin/bash
echo "QUIT" | openssl s_client -starttls smtp -connect YOUR_HOST:25 2>/dev/null | grep -q "STARTTLS" || echo "STARTTLS not configured"
