#!/usr/bin/python3
""" defines a class for Student """


class Student:
    """ student class """

    def __init__(self, first_name, last_name, age):
        """
        initialize Student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a
        Student instance
        """
        if (type(attrs) == list and all(type(attr) == str for attr in attrs)):
            return {v: getattr(self, v) for v in attrs if hasattr(self, v)}
        return self.__dict__
