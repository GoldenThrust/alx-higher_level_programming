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
        retrieves a dictionary representation of a Student instance
        """
        if (type(attrs) == list and all(type(attr) == str for attr in attrs)):
            return {val: getattr(self, val) for val in attrs if hasattr(self, val)}
        return self.__dict__

    def reload_from_json(self, json):
        """
         replaces all attributes of the Student instance
        """
        for i, j in json.items():
            setattr(self, i, j)

