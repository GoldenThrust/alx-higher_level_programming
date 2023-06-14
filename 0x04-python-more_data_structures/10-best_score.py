#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary == {} or a_dictionary is None:
        return None
    biggest_value = max(a_dictionary.values())
    for key, value in a_dictionary.items():
        if value is biggest_value:
            return key
