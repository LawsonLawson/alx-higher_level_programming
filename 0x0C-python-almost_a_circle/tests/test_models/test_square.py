#!/usr/bin/python3


"""
Module: test_square.py

Description: This module features a unittest for the "Square" class.
"""


import unittest
import sys
import io
import contextlib
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquareClass(unittest.TestCase):
    """
    Contains multiple testing methods for the Square class
    """

    def setUp(self):
        """
        To reset __nb_objects
        """
        Base._Base__nb_objects = 0

    def test_checkInheritance(self):
        """
        Test case to check if a Square instance inherits from Rectangle
        """
        self.assertIsInstance(Square(5), Rectangle)

    def test_createRegular(self):
        """
        Test case to create a Square instance with all regular values
        """
        sq1 = Square(20, 8, 9, 999)
        self.assertEqual(str(sq1), "[Square] (999) 8/9 - 20")

    def test_createRegular2(self):
        """
        Test case to create a Square instance with just size
        """
        sq2 = Square(55)
        self.assertEqual(str(sq2), "[Square] (1) 0/0 - 55")

    def test_sizeError(self):
        """
        Test case to create a Square instance with size as a string
        """
        with self.assertRaises(TypeError):
            Square("sizee")

    def test_sizeError2(self):
        """
        Test case to create a Square instance with size as a negative value
        """
        with self.assertRaises(ValueError):
            Square(-96)

    def test_xError(self):
        """
        Test case to create a Square instance with x as a string
        """
        with self.assertRaises(TypeError):
            Square(3, "Ex", 6)

    def test_xError2(self):
        """
        Test case to create a Square instance with x as a negative value
        """
        with self.assertRaises(ValueError):
            Square(3, -6, 6)

    def test_yError(self):
        """
        Test case to create a Square instance with y as a string
        """
        with self.assertRaises(TypeError):
            Square(3, 2, "trees")

    def test_yError2(self):
        """
        Test case to create a Square instance with y as a negative value
        """
        with self.assertRaises(ValueError):
            Square(3, 2, -3)

    def test_area(self):
        """
        Test case to calculate the area of a Square
        """
        sq3 = Square(4)
        self.assertEqual(sq3.area(), 16)

    def test_width_height_validation_inherited(self):
        """
        Test case to ensure width, height, x, and y validation is inherited
        from Rectangle
        """
        with self.assertRaises(ValueError):
            Square(0)

        with self.assertRaises(ValueError):
            Square(-5, -1, -1)

    def test_data_consistency(self):
        """
        Test case to ensure data consistency in to_dictionary and
        from_json_string methods
        """
        sq = Square(5, 2, 3, 999)
        sq_dict = sq.to_dictionary()
        sq_json_str = Square.to_json_string([sq_dict])
        sq_json_dict = json.loads(sq_json_str)

        self.assertEqual(sq_dict, sq_json_dict[0])

    def test_methods_inherited_from_rectangle(self):
        """
        Test case to check methods inherited from Rectangle.
        """
        sq = Square(4)
        self.assertEqual(sq.area(), 16)
        sq.update(7)
        self.assertEqual(sq.id, 7)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            sq.display()
        s = f.getvalue()
        res = "####\n####\n####\n####\n"
        self.assertEqual(s, res)

    def test_update_with_positional_and_keyword_arguments(self):
        """
        Test case to check if the update method works correctly
        with both positional and keyword arguments.
        """
        sq = Square(5)
        sq.update(10)
        self.assertEqual(sq.id, 10)
        sq.update(x=12)
        self.assertEqual(sq.x, 12)
        sq.update(size=7, id=89, y=1)
        self.assertEqual(sq.size, 7)
        self.assertEqual(sq.id, 89)
        self.assertEqual(sq.y, 1)
        sq.update()
        self.assertEqual(sq.size, 7)
        self.assertEqual(sq.id, 89)
        self.assertEqual(sq.y, 1)

    def test_size_zero(self):
        """
        Test case to create a Square instance with size zero
        """
        with self.assertRaises(ValueError):
            Square(0)

    def test_large_size(self):
        """
        Test case to create a Square instance with a large size
        """
        sq = Square(sys.maxsize)
        self.assertEqual(sq.size, sys.maxsize)

    def test_negative_coordinates(self):
        """
        Test case to create a Square instance with negative x and y coordinates
        """
        with self.assertRaises(ValueError):
            Square(5, -1, -1)

    def test_negative_size(self):
        """
        Test case to create a Square instance with negative size
        """
        with self.assertRaises(ValueError):
            Square(-5)

    def test_invalid_size_type(self):
        """
        Test case to create a Square instance with size as a string
        """
        with self.assertRaises(TypeError):
            Square("sizee")

    def test_invalid_x_type(self):
        """
        Test case to create a Square instance with x as a string
        """
        with self.assertRaises(TypeError):
            Square(3, "Ex", 6)

    def test_invalid_y_type(self):
        """
        Test case to create a Square instance with y as a string
        """
        with self.assertRaises(TypeError):
            Square(3, 2, "trees")


if __name__ == '__main__':
    unittest.main()
