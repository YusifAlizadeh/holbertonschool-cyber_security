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

    try:
        # Поиск сегмента кучи
        with open(maps_path, "r") as maps_file:
            heap = None
            for line in maps_file:
                if "[heap]" in line:
                    heap = line
                    break

            if not heap:
                return

            # Парсинг диапазона адресов
            addr_range = heap.split()[0].split("-")
            heap_start = int(addr_range[0], 16)
            heap_end = int(addr_range[1], 16)

        # Чтение и замена в памяти
        with open(mem_path, "r+b") as mem_file:
            mem_file.seek(heap_start)
            heap_data = mem_file.read(heap_end - heap_start)

            offset = heap_data.find(search_string)
            if offset == -1:
                return

            # Запись новой строки
            mem_file.seek(heap_start + offset)
            mem_file.write(replace_string)
            
            # ВАЖНО: Выводим SUCCESS! только один раз здесь
            print("SUCCESS!")

    except (PermissionError, FileNotFoundError, Exception):
        sys.exit(1)


def main():
    # Проверка количества аргументов (Usage error -> status 1)
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
