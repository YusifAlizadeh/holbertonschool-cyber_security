#!/bin/bash
grep -E "iptables|ufw" auth.log | grep -E "\-A|\-I|allow|deny|add" | wc -l
