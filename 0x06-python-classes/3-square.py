#!/usr/bin/python3
""" Class Square """


class Square:
    """ set Method for Class """

    def __init__(self, size=0):
        """ Initialize Squaare
        Args:
            size (int): size of square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
            """ Return area of a square """
            return self.__size ** 2
