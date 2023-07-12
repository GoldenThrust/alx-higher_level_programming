#!/usr/bin/python3
"""
MyInt Class
"""


class MyInt(int):
    """ Inherit from int """

    def __eq__(self, value):
        """
        Invert equal to
        """
        return self.real != value

    def __ne__(self, value):
        """
        Invert not equal to
        """
        return self.real == value
