#!/usr/bin/python3
""" Defines Square model class """

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This Represents the Square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new Square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        set the size of the Square
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        set the size of the Square
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ 
        Update the Rectangle
        """
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1

        elif kwargs and len(kwargs) != 0:
            for i, j in kwargs.items():
                if i == "id":
                    if j is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = j
                elif i == "size":
                    self.size = j
                elif i == "x":
                    self.x = j
                elif i == "y":
                    self.y = j

    def to_dictionary(self):
        """
        Return the dictionary representation of a Rectangle
        """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """ string representation of the Square """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

