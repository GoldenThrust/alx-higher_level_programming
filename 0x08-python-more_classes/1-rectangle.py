#!/usr/bin/python3
""" Rectangle class """


class Rectangle:
    """ rectangle interface """

    def __init__(self, width=0, height=0):
        """ initiakized rectangle """
        self.__height = height
        self.__width = width

        @property
        def width(self):
            """ get rectangle widh """
            return self.__width

        @width.setter
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            """ get rectangle height """
            return self.__height

        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
