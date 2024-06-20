#!/usr/bin/python3
"""
    Write a script that reads stdin
    line by line and computes metrics
"""
import sys


import sys
import re
from collections import defaultdict

total_size = 0
status_counts = defaultdict(int)

line_count = 0
try:
    for line in sys.stdin:
        line_count += 1
        match = re.match(r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*)\] "GET (.*) HTTP/1\.1" (\d+) (\d+)$', line)
        if match:
            status_code = int(match.group(4))
            file_size = int(match.group(5))
            total_size += file_size
            status_counts[status_code] += 1
            if line_count % 10 == 0:
                print("Total file size: {}".format(total_size))
                print("Number of lines by status code:")
                for status_code in sorted(status_counts.keys()):
                    print("{}: {}".format(status_code, status_counts[status_code]))
                print()
except KeyboardInterrupt:
    print("Total file size: {}".format(total_size))
    print("Number of lines by status code:")
    for status_code in sorted(status_counts.keys()):
        print("{}: {}".format(status_code, status_counts[status_code]))
    print()
