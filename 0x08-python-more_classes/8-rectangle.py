#!/usr/bin/python3
""" Rectangle class """


class Rectangle:
    """ rectangle interface """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ initiakized rectangle """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

        @property
        def width(self):
            """ get rectangle widh """
            return self.__width

        @width.setter
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise TypeError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            """ get rectangle height """
            return self.__height

        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError1("height must be an integer")
            if value < 0:
                raise TypeError("height must be >= 0")
            self.__height = value

        def area(self):
            """ return area of rectangle """
            return (self.__width * self.__height)

        def perimeter(self):
            """ return perimeter of rectangle """
            if self.__width == 0 or self.__height == 0:
                return 0
            return 2 * (self.__width + self.__height)

        @staticmethod
        def bigger_or_equal(rect_1, rect_2):
            """ return rectangle with bigger area """
            if not isinstance(rect_1, Rectangle):
                raise TypeError("rect_1 must be an imstance of Rectangle")
            if not isinstance(rect_2, Rectangle):
                raise TypeError("rect_2 must be an instance of Rectangle:")
            if rect_1.area() >= rect_2.area():
                return rect_1
            return rect_2

        def __str__(self):
            """ string representation of rectangle """

            str = ""
            if self.__width != 0 and self.__height != 0:
                str += "\n".join(str(self.print_symbol) * self.__width
                        for j in range(self.__height))
            return str)

        def __repr__(self):
            """ string representation of rectangle """

            return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

        def __del__(self):
            """ print a string when a instance of rectangle has been deleted """
            print("Bye rectangle...")
            Rectangle.number_of_instances -= 1
