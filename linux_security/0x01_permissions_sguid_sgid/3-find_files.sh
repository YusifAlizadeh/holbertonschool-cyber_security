#!/bin/bash
find "$1" -type f \( -perm -4000 -o -perm -2000 \) -print0 2>/dev/null | xargs -0 ls -l
