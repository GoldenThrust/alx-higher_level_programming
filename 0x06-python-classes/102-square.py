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

    def __eq__(self, other):
        """equal to comparision to Square """
        return self.area() == other.area()

    def __ne__(self, other):
        """ not equal comparison to Square """
        return self.area() != other.area()

    def __lt__(self, other):
        """ less than comparison to Square """
        return self.area() < other.area()

    def __le__(self, other):
        """ less than or equal to comparison to Square """
        return self.area() <= other.area()

    def __gt__(self, other):
        """ greater than comparison to Square """
        return self.area() > other.area()

    def __ge__(self, other):
        """ greater than or equal to compmarison to Square """
        return self.area() >= other.area()

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
