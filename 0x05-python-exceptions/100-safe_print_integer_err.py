#!/usr/bin/python3
import sys as s


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        print("Exception: {}".format(s.exc_info()[1]), file=s.stderr)
        return False
