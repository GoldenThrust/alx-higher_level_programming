#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """ getter and setter for the square property """
    def __init__(self, size=0):
        """ initializes square
        Args:
            size (int): size of square"""
        self.size = size

    def area(self):
        """ Return area of square """
        return (self.__size) ** 2

    @property
    def size(self):
        """ __size getter """
        return self.__size

    @size.setter
    def size(self, value):
        """ __size setter """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
