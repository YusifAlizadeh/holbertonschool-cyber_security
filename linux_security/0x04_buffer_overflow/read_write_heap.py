#!/usr/bin/python3
"""
read_write_heap.py - Script to search and replace a string in
the heap of a running process.
"""

import sys
import os


def find_and_replace_in_heap(pid, search_string, replace_string):
    maps_path = f"/proc/{pid}/maps"
    mem_path = f"/proc/{pid}/mem"

    try:и
        with open(maps_path, "r") as maps_file:
            heap = None
            for line in maps_file:
                if "[heap]" in line:
                    heap = line
                    break

            if not heap:
                return
�в
            addr_range = heap.split()[0].split("-")
            heap_start = int(addr_range[0], 16)
            heap_end = int(addr_range[1], 16)
и
        with open(mem_path, "r+b") as mem_file:
            mem_file.seek(heap_start)
            heap_data = mem_file.read(heap_end - heap_start)

            offset = heap_data.find(search_string)
            if offset == -1:
                return
�ки
            mem_file.seek(heap_start + offset)
            mem_file.write(replace_string)
           print("SUCCESS!")

    except (PermissionError, FileNotFoundError, Exception):
        sys.exit(1)


def main():
    if len(sys.argv) != 4:
        print("Usage: read_write_heap.py pid search_string replace_string")
        sys.exit(1)

    try:
        pid = int(sys.argv[1])
    except ValueError:
        print("Usage: read_write_heap.py pid search_string replace_string")
        sys.exit(1)

    search_string = sys.argv[2].encode()
    replace_string = sys.argv[3].encode()

    find_and_replace_in_heap(pid, search_string, replace_string)


if __name__ == "__main__":
    main()
