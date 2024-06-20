#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics.
"""
import sys
import signal

total_size = 0
status_counts = {
    200: 0, 301: 0, 400: 0, 401: 0,
    403: 0, 404: 0, 405: 0, 500: 0
}
line_count = 0


def print_stats():
    """Print the current statistics."""
    global total_size, status_counts
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))


def signal_handler(sig, frame):
    """Handle the interrupt signal to print stats before exiting."""
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        try:
            parts = line.split()
            print(f"Processing parts: {parts}")  # Debug print

            if len(parts) < 9:
                print(f"Skipped line (too few parts): {line.strip()}")  # Debug print
                continue

            ip = parts[0]
            dash = parts[1]
            date = parts[2] + " " + parts[3] + " " + parts[4]
            method = parts[5]
            path = parts[6]
            protocol = parts[7]
            status_code = parts[8]
            file_size = parts[9]

            print(f"Parsed line: {method} {path} {protocol} {status_code} {file_size}")  # Debug print

            if (method != '"GET' or
                    path != '/projects/260' or
                    protocol != 'HTTP/1.1"'):
                print(f"Skipped line (incorrect format): {line.strip()}")  # Debug print
                continue

            status_code = int(status_code)
            file_size = int(file_size)

            total_size += file_size
            if status_code in status_counts:
                status_counts[status_code] += 1
            line_count += 1

            if line_count % 10 == 0:
                print_stats()

        except Exception as e:
            print(f"Exception while processing line: {line.strip()}, Error: {str(e)}")  # Debug print
            continue

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)
