#!/bin/bash
grep "Accepted" auth.log | grep -v "root" | awk '{print $(NF-3)}' | sort -u | wc -l
