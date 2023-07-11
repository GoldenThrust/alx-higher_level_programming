#!/usr/bin/python3
"""
    Rectangle inherite from 7-base_geometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
     Rectangle using BaseGeometry
    """

    def __init__(self, width, height):
        """
        initialized Rectangle
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """ Return the area of the rectangle """
        return self.__width * self.__height

    def __str__(self):
        """
        Return the str() representation of a Rectangle
        """
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string

