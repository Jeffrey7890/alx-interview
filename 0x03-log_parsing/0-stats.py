#!/usr/bin/python3

""" parsing status code from server """

import re
import sys
import signal
import time
from collections import defaultdict


signal.signal(signal.SIGPIPE, signal.SIG_DFL)
pattern = (
    r'^((?:\d{1,3}\.){3}\d{1,3})'   # IP address
    r'\s-\s'                        # Space, dash, space
    r'\[(.*?)\]'                    # Date inside square brackets
    r'\s"GET\s/projects/260\sHTTP/1\.1"\s'  # GET request
    r'([1-5]\d{2})'                 # Status code (e.g., 200, 404)
    r'\s(\d+)$'                     # File size
)

pattern = re.compile(pattern)
status_dict = defaultdict(int)
status_dict['file_total'] = 0
sorted_status = set()


def get_input_line() -> str:
    """ reads line from stdin """
    return (sys.stdin.readline())


def parse_line(line: str) -> dict:
    """ parses the line for input """
    global pattern
    if "GET /projects/260 HTTP/1.1" not in line:
        return None
    match = pattern.match(line)
    if match:
        ip_address = match.group(1)
        date = match.group(2)
        status_code = match.group(3)
        file_size = match.group(4)
        return ({
            'ip_address': ip_address,
            'date': date,
            'status_code': status_code,
            'file_size': file_size
            })
    else:
        return (None)


def print_status(status_d, s_status):
    """ print the status of line """
    total = status_d['file_total']
    sys.stdout.write(f'File size: {total}\n')
    for statuss in sorted(s_status):
        count = status_dict[statuss]
        sys.stdout.write(f'{statuss}: {count}\n')


def sigint_handler(signum, frame):
    """ handles Ctrl+C signal """
    global sorted_status
    global status_dict
    print_status(status_dict, sorted_status)
    raise KeyboardInterrupt


def main():
    """ main loop """
    global sorted_status
    cnt = 1
    for i in range(10000):
        cnt += 1
        parsed_log = parse_line(get_input_line())
        if (parsed_log is not None):
            status = parsed_log['status_code']
            size = parsed_log['file_size']
            if status.isdigit():
                status_dict[status] += 1
                sorted_status.add(status)
            if size.isdigit():
                status_dict['file_total'] += int(size)

            if (cnt == 10):
                print_status(status_dict, sorted_status)
                sorted_status = set()
                cnt = 0


if __name__ == "__main__":
    signal.signal(signal.SIGINT, sigint_handler)

    main()
