#!/usr/bin/python3
"""
Defines unittests for base.py.
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of the Base class
    """

    def test_zero_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_id(self):
        self.assertEqual(20, Base(20).id)

    def test_nb_instances_isprivate(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(3, 5)


class TestBase_to_json_string(unittest.TestCase):
    """
    Unittests for testing to_json_string method of Base class
    """
    
    def test_rectangle(self):
        rect = Rectangle(20, 10, 2, 2, 1)
        self.assertEqual(str, type(Base.to_json_string([rect.to_dictionary()])))

    def test_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

class TestBase_save_to_file(unittest.TestCase):
    """
    Unittests for testing save_to_file method of Base class
    """

    @classmethod
    def tearDown(self):
        """ Delete all created files """
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_rectangle(self):
        rect = Rectangle(20, 10, 2, 2, 1)
        Rectangle.save_to_file([rect])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)

    def test_square(self):
        squ = Square(20, 10, 2, 1)
        Square.save_to_file([squ])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_None(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()


class TestBase_from_json_string(unittest.TestCase):
    """
    Unittests for testing from_json_string method of Base class
    """
    def test_rectangle(self):
        lists = [{"id": 1, "width": 20, "height": 20, "x": 10}]
        to_json = Rectangle.to_json_string(lists)
        from_json = Rectangle.from_json_string(to_json)
        self.assertEqual(list, from_json)

    def test_square(self):
        list_input = [{"id": 1, "size": 10, "height": 40}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_None(self):
        self.assertEqual([], Base.from_json_string(None))


class TestBase_create(unittest.TestCase):
    """
    Unittests for testing create method of Base class
    """

    def test_rectangle(self):
        rect1 = Rectangle(20, 10, 3, 5, 1)
        r1_dictionary = rect1.to_dictionary()
        rect2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (1) 3/5 - 20/10", str(rect2))


    def test_square(self):
        squ1 = Square(10, 3, 5, 1)
        s1_dictionary = squ1.to_dictionary()
        squ2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (1) 3/5 - 10", str(squ2))


class TestBase_load_from_file(unittest.TestCase):
    """
    Unittests for testing load_from_file_method of Base class
    """

    @classmethod
    def tearDown(self):
        """Delete all created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_rectangle(self):
        rect1 = Rectangle(10, 7, 2, 8, 1)
        rect2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([rect1, rect2])
        output = Rectangle.load_from_file()
        self.assertEqual(str(rect1), str(output[0]))


    def test_square(self):
        squ1 = Square(5, 1, 3, 3)
        squ2 = Square(9, 5, 2, 3)
        Square.save_to_file([squ1, squ2])
        output = Square.load_from_file()
        self.assertEqual(str(squ1), str(output[0]))

    def test_no_file(self):
        output = Square.load_from_file()
        self.assertEqual([], output)

    def test_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)


class TestBase_save_to_file_csv(unittest.TestCase):
    """
    Unittests for testing save_to_file_csv method of Base class
    """

    @classmethod
    def tearDown(self):
        """Delete all created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass
        try:
            os.remove("Base.csv")
        except IOError:
            pass

    def test_rectangle(self):
        rect = Rectangle(20, 10, 2, 3, 1)
        Rectangle.save_to_file_csv([rect])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("1,20,10,2,3", f.read())

    def test_square(self):
        squ = Square(20, 10, 3, 1)
        Square.save_to_file_csv([squ])
        with open("Square.csv", "r") as f:
            self.assertTrue("1,20,10,3", f.read())

    def test_None(self):
        Square.save_to_file_csv(None)
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()


class TestBase_load_from_file_csv(unittest.TestCase):
    """
    Unittests for testing load_from_file_csv method of Base class
    """

    @classmethod
    def tearDown(self):
        """ Delete all created files """
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass

    def test_rectangle(self):
        rect1 = Rectangle(10, 7, 2, 8, 1)
        rect2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([rect1, rect2])
        output = Rectangle.load_from_file_csv()
        self.assertEqual(str(rect1), str(output[0]))

    def test_square(self):
        squ1 = Square(5, 1, 3, 3)
        squ2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([squ1, squ2])
        output = Square.load_from_file_csv()
        self.assertEqual(str(squ1), str(output[0]))

    def test_zero_file(self):
        output = Square.load_from_file_csv()
        self.assertEqual([], output)

    def test_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 1)


if __name__ == "__main__":
    unittest.main()

