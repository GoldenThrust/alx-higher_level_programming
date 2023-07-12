#!/usr/bin/python3
""" define a function that to object to json string """
import json


def to_json_string(my_obj):
    """ returns the JSON representation of an object (string) """
    return json.dumps(my_obj)
