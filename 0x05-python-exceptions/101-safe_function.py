#!/usr/bin/python3
import sys as s


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=s.stderr)
        return None
    else:
        return result
