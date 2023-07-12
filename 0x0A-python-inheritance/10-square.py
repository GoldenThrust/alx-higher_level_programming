#!/usr/bin/python3
""" Rectangle inherite from 9-rectangle """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ square using class Rectangle """

    def __init__(self, size):
        """
        Initialize square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
