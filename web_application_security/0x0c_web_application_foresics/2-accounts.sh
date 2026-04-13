#!/bin/bash
tail -n 1000 auth.log | grep -E "root" | awk '{print $9}' | head -n 1
