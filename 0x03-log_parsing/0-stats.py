#!/usr/bin/python3
"""
    Log parsing
"""
import sys
import re

file_size = 0
status_codes = {}

try:
    for i, line in enumerate(sys.stdin):
        pattern = (
            r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[.*\] "
            r"\"GET /projects/260 HTTP/1.1\" (\d+) (\d+)$"
        )

        match = re.match(pattern, line)

        if match:
            file_size += int(match.group(2))
            status_code = int(match.group(1))
            if status_code in status_codes:
                status_codes[status_code] += 1
            else:
                status_codes[status_code] = 1

        if (i + 1) % 10 == 0:
            print("File size:", file_size)
            for status_code in sorted(status_codes.keys()):
                print(f"{status_code}: {status_codes[status_code]}")

except KeyboardInterrupt:
    print("File size:", file_size)
    for status_code in sorted(status_codes.keys()):
        print(f"{status_code}: {status_codes[status_code]}")
