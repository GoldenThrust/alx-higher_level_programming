#!/usr/bin/python3
""" Class Square """


class Square:
    """ Square oops function """

    def __init__(self, size=0, position=(0, 0)):
        """ Initialize square """
        self.size = size
        self.position = position

    def area(self):
        """ Return area of square """
        return (self.__size) ** 2

    def my_print(self):
        """ Print square with # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for j in range(self.__position[0])]
            [print("#", end="") for k in range(self.__size)]
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

    @property
    def position(self):
        """__position getter"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """__position setter"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def __str__(self):
        """ string representation of a Square """
        if self.__size != 0:
            [print("") for i in range(self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for j in range(self.__position[0])]
            [print("#", end="") for k in range(self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
