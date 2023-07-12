#!/usr/bin/python3
""" 
script that adds all arguments to a Python list,
and then save them to a file
"""
import sys

if __name__ == "__main__":
    save_json = __import__('5-save_to_json_file').save_to_json_fie
    load_json = __import__('6-load_from_json_file').load_from_json_file

    try:
        argv = load_json("add_item.json")
    except FileNotFoundError:
        argv = []
    argv.extend(sys.argv[1:])
    save_json(argv, "add_item.json")

