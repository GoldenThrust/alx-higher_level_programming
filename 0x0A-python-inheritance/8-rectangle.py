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
