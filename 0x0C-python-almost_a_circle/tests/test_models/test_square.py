#!/usr/bin/python3

"""
Defines unittests for models/square.py.
"""
import io
import sys
import unittest
from models.base import Base
from models.square import Square


class TestSquare_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Square class."""

    def test_is_base(self):
        self.assertIsInstance(Square(10), Base)

    def test_is_rectangle(self):
        self.assertIsInstance(Square(10), Square)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_arg(self):
        squ1 = Square(3)
        squ2 = Square(4)
        self.assertEqual(squ1.id, squ2.id - 1)

class TestSquare_area(unittest.TestCase):
    """Unittests for testing the area method of the Square class."""

    def test_area(self):
        self.assertEqual(100, Square(10, 2, 2, 1).area())

    def test_arg(self):
        squ = Square(10, 2, 2, 1)
        with self.assertRaises(TypeError):
            squ.area(1)


class TestSquare_stdout(unittest.TestCase):
    """
    Unittests for testing __str__ and display methods of Square class
    """

    def test_str_method(self):
        squ = Square(20, 2, 2, 1)
        self.assertEqual("[Square] (1) 2/2 - 20", str(squ))

class TestSquare_to_dictionary(unittest.TestCase):
    """
    Unittests for testing to_dictionary method of the Square class
    """

    def test_output(self):
        squ = Square(20, 2, 2, 1)
        diction = {'id': 1, 'x': 2, 'y': 2, 'size': 20}
        self.assertDictEqual(diction, squ.to_dictionary())

    def test__arg(self):
        squ = Square(10, 2, 2, 1)
        with self.assertRaises(TypeError):
            squ.to_dictionary(1)

if __name__ == "__main__":
    unittest.main()

