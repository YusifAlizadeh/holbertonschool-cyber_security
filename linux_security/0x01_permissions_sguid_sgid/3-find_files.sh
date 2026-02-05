#!/bin/bash
find "$1" -type f -perm /6000 -printf "%M %n %u %g %s %b %t %p\n" 2>/dev/null
