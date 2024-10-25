#!/usr/bin/env python3

"""Script for parsing status codes and computing metrics from logs."""

import sys
import re
import signal

# Initialize global variables to store metrics
total_file_size = 0
status_dict = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}
line_count = 0

# Compile the pattern to match the expected log line format
pattern = re.compile(
    r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] '
    r'"GET /projects/260 HTTP/1\.1" ([1-5]\d{2}) (\d+)$'
)


def print_statistics():
    """Print accumulated file size and count of each status code."""
    global total_file_size, status_dict
    print(f"File size: {total_file_size}")
    for status_code in sorted(status_dict.keys()):
        if status_dict[status_code] > 0:
            print(f"{status_code}: {status_dict[status_code]}")


def sigint_handler(signum, frame):
    """Handle keyboard interrupt and print statistics."""
    print_statistics()
    sys.exit(0)


def process_line(line):
    """
    Parse and process each log line.
    Update the total file size and status code counts.
    """
    global total_file_size, status_dict, line_count

    match = pattern.match(line)
    if match:
        status_code = match.group(3)
        file_size = match.group(4)

        total_file_size += int(file_size)

        if status_code in status_dict:
            status_dict[status_code] += 1

        line_count += 1

        if line_count % 10 == 0:
            print_statistics()


if __name__ == "__main__":
    # Set signal handler for CTRL + C (SIGINT)
    signal.signal(signal.SIGINT, sigint_handler)

    try:
        # Process each line from stdin
        for line in sys.stdin:
            process_line(line.strip())
    except KeyboardInterrupt:
        # Handle any remaining statistics before exit
        print_statistics()
        sys.exit(0)

    # Print final statistics after EOF
    print_statistics()
