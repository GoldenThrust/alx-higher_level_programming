#!/usr/bin/python3
# test_rectangle.py
# Brennan D Baraban <375@holbertonschool.com>
"""
Defines unittests for models/rectangle.py.
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_instantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of the Rectangle class
    """

    def test_rectangle_isbase(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

class TestRectangle_area(unittest.TestCase):
    """
    Unittests for testing the area method of the Rectangle class
    """

    def test_area(self):
        rect = Rectangle(30, 20, 2, 2, 1)
        self.assertEqual(600, rect.area())

    def test_arg(self):
        rect = Rectangle(2, 10, 1, 1, 1)
        with self.assertRaises(TypeError):
            rect.area(2)


class TestRectangle_stdout(unittest.TestCase):
    """
    Unittests for testing __str__ and display methods of Rectangle class
    """

    def test_str_method(self):
        rect = Rectangle(20, 10, 2, 3, 1)
        self.assertEqual("[Rectangle] (1) 2/3 - 20/10", str(rect))


class TestRectangle_to_dictionary(unittest.TestCase):
    """
    Unittests for testing to_dictionary method of the Rectangle class
    """

    def test_output(self):
        rect = Rectangle(20, 10, 2, 3, 1)
        diction = {'id': 1, 'x': 2, 'y': 3, 'width': 20, 'height': 10}
        self.assertDictEqual(diction, rect.to_dictionary())


    def test_arg(self):
        rect = Rectangle(20, 10, 2, 3, 1)
        with self.assertRaises(TypeError):
            rect.to_dictionary(1)

if __name__ == "__main__":
    unittest.main()

