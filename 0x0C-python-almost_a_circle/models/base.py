#!/usr/bin/python3

""" Defines Base model class """
import json
import csv
import turtle


class Base:
    """
    This Represents the Base
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON serialization of a list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON serialization of a list_objs to a file.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                dicts = [i.to_dictionary() for i in list_objs]
                file.write(Base.to_json_string(dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Return the deserialization of a json_string
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                init_class = cls(1, 1)
            else:
                init_class = cls(1)
            init_class.update(**dictionary)
            return init_class

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(i) for i in dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Write the CSV serialization of a list_objs into a file.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as file:
            if list_objs is None or list_objs == []:
                file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    attr = ["id", "width", "height", "x", "y"]
                else:
                    attr = ["id", "size", "x", "y"]
                dict_writer = csv.DictWriter(file, fieldnames=attr)
                for i in list_objs:
                    dict_writer.writerow(i.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Return a list of classes instantiated from a CSV file.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as file:
                if cls.__name__ == "Rectangle":
                    attr = ["id", "width", "height", "x", "y"]
                else:
                    attr = ["id", "size", "x", "y"]
                dicts = csv.DictReader(file, fieldnames=attr)
                dicts = [dict([i, int(j)] for i, j in k.items())
                         for k in dicts]
                return [cls.create(**i) for i in dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draw Rectangles and Squares using the turtle
        """
        screen = turtle.Screen()
        screen.title("Drawing Rectangles and Squares Using turtle")
        screen.setup(800, 800)
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.pensize(2)

        # Draw rectangles
        for i, rectangle in enumerate(list_rectangles):
            pen.penup()
            pen.goto(rectangle.x, rectangle.y)
            pen.pendown()

            pen.color("blue")
            for _ in range(2):
                pen.forward(rectangle.width)
                pen.left(90)
                pen.forward(rectangle.height)
                pen.left(90)

        # Draw squares
        for i, square in enumerate(list_squares):
            pen.penup()
            pen.goto(square.x, square.y)
            pen.pendown()

            pen.color("pink")

            for _ in range(2):
                pen.forward(square.width)
                pen.left(90)
                pen.forward(square.height)
                pen.left(90)

        turtle.done()
        turtle.exitonclick()
