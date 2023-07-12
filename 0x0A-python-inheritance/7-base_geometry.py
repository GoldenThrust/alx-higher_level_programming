#!/usr/bin/python3
""" Base Geometry """

class BaseGeometry:
    """ base geometry """

    def area(self):
        """ area that raise an exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate value
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
