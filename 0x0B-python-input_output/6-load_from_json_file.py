#!/usr/bin/python3
"""
    define a function that create an object from
    a JSON file
"""
import json


def load_from_json_file(filename):
    """ creates an Object from a “JSON file """
    with open(filename) as f:
        return json.load(f)
