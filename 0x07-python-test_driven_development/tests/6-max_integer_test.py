#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ unittest class for max_integer """
    def test_empty(self):
        """ Tests for empty list """
        t = []
        self.assertIsNone(max_integer(t))

    def test_zero_args(self):
        """ Tests for zero argument """
        self.assertIsNone(max_integer())

    def test_one_args(self):
        """ Test for one number in a list """
        t = [1]
        self.assertEqual(max_integer(t), 1)

    def test_middle(self):
        """ Tests for max in middle"""
        t = [33, 46, 589, 66, 77]
        self.assertEqual(max_integer(t), 589)

    def test_negative(self):
        """ Tests for negative numbers in list """
        t = [-589, -566 -87, -1, -566]
        self.assertEqual(max_integer(t), -1)

    def test_non_int_arg(self):
       """ Tests for a non integer in list """
        t = ["gold", 56, 97, 88]
        with self.assertRaises(TypeError):
            max_integer(t)

if __name__ == "__main__":
    unittest.main()
