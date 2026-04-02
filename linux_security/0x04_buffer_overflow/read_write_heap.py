#!/usr/bin/python3
"""
Module to find and replace a string in the heap of a running process.
"""
import sys

def usage():
    print("Usage: ./read_write_heap.py pid search_string replace_string")
    sys.exit(1)

def read_write_heap(pid, search_string, replace_string):
    try:
        pid = int(pid)
    except ValueError:
        usage()

    maps_path = f"/proc/{pid}/maps"
    mem_path = f"/proc/{pid}/mem"

    try:
        with open(maps_path, "r") as maps_file:
            heap = None
            for line in maps_file:
                if "[heap]" in line:
                    heap = line
                    break
            if not heap:
                sys.exit(1)

            heap_start, heap_end = [int(x, 16) for x in heap.split()[0].split("-")]

        with open(mem_path, "r+b") as mem_file:
            mem_file.seek(heap_start)
            heap_data = mem_file.read(heap_end - heap_start)

            search_bytes = search_string.encode()
            replace_bytes = replace_string.encode()

            if len(replace_bytes) > len(search_bytes):
                sys.exit(1)

            offset = heap_data.find(search_bytes)
            if offset == -1:
                sys.exit(1)

            mem_file.seek(heap_start + offset)
            mem_file.write(replace_bytes.ljust(len(search_bytes), b'\x00'))

            print("SUCCESS!")

    except (PermissionError, FileNotFoundError, Exception):
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        usage()
    pid = sys.argv[1]
    search_string = sys.argv[2]
    replace_string = sys.argv[3]

    read_write_heap(pid, search_string, replace_string)
