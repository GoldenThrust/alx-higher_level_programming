#!/usr/bin/python3
"""
conMyLIst Class
"""


class MyList(list):
    """ Myist """
    def __init__(self):
        """ initializes MyList """
        super().__init__()

    def print_sorted(self):
        """ prints the sorted list """
        print(sorted(self))

