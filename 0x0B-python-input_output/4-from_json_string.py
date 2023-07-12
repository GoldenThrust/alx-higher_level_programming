#!/usr/bin/python3
""" define a function that turn json string to object """
import json


def from_json_string(my_str):
    """ returns an object
    (Python data structure) represented by a JSON string """
    return json.loads(my_str)
