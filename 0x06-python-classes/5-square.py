#!/usr/bin/python3
""" class Square """


class Square:
    """ Square interface """

    def __init__(self, size):
        """ Initialize square
        Args:
            size (int): size of square"""
        self.size = size

    def area(self):
        """ Return area of square """
        return self.__size ** 2

    def my_print(self):
        """ Print square with the # character """

        if self.__size == 0:
            print()
            return

        for i in range(self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")

    @property
    def size(self):
        """ __size getter """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ __size setter """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
