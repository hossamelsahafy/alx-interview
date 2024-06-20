#!/usr/bin/python3
"""
     script that reads stdin line
     by line and computes metrics
"""
import sys
import signal

total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_stats():
    """Print State"""
    global total_size, status_counts
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))

def signal_handler(sig, frame):
    """
        signal_handler
    """
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        try:
            parts = line.split()
            if len(parts) < 7:
                continue
            ip, dash, date, method, path, protocol, status_code, file_size = parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6], parts[7]
            if method != '"GET' or path != '/projects/260' or protocol != 'HTTP/1.1"':
                continue
            status_code = int(status_code)
            file_size = int(file_size)
            
            total_size += file_size
            if status_code in status_counts:
                status_counts[status_code] += 1
            line_count += 1

            if line_count % 10 == 0:
                print_stats()

        except Exception:
            continue

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)
