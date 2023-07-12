#!/usr/bin/python3
"""
define function that read from standard input
and compute status metric.
"""


def print_stats(file_size, status_codes):
    """
    reads stdin line by line and computes metrics
    """
    print("File size:", file_size)
    for code in sorted(status_codes):
        print(code + ":", status_codes[code])


if __name__ == "__main__":
    import sys

    file_size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(file_size, status_codes)
                count = 1
            else:
                count += 1

            split_line = line.split()

            try:
                file_size += int(split_line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if split_line[-2] in valid_codes:
                    status_codes[split_line[-2]] = status_codes.get(split_line[-2], 0) + 1
            except IndexError:
                pass

        print_stats(file_size, status_codes)

    except KeyboardInterrupt:
        print_stats(file_size, status_codes)
        raise
