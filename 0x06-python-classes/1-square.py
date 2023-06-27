#!/usr/bin/python3
""" Class Square """


class Square:
    """ class with private size attribute """

    def __init__(self, size):
        """ initialize Square
        Args:
            size (int): size of the new square
            """
        self.__size = size
