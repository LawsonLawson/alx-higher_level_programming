#!/usr/bin/python3


"""
Module: test_rectangle.py

Desctiption: This module features a unittest for the "Rectangle" class.
"""


import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """
    Contains multiple testing methods for the Rectangle class.
    """

    def setUp(self):
        """
        Sets up necessary configurations before each test method runs.
        """
        Base._Base__nb_objects = 0

    def test_checkInheritance(self):
        """
        Test if a Rectangle instance inherits from Base.
        """
        self.assertIsInstance(Rectangle(5, 8), Base)

    def test_createRegular(self):
        """
        Test creating a Rectangle instance with all regular values.
        """
        rect1 = Rectangle(2, 4, 8, 9, 999)
        self.assertEqual(str(rect1), "[Rectangle] (999) 8/9 - 2/4")

    def test_createRegular2(self):
        """
        Test creating a Rectangle instance with just width and height.
        """
        rect2 = Rectangle(70, 50)
        self.assertEqual(str(rect2), "[Rectangle] (1) 0/0 - 70/50")

    def test_widthError(self):
        """
        Test creating a Rectangle instance with width as a string.
        """
        with self.assertRaises(TypeError):
            Rectangle("bleh", 50)

    def test_widthError2(self):
        """
        Test creating a Rectangle instance with width as a negative value.
        """
        with self.assertRaises(ValueError):
            Rectangle(-43, 50)

    def test_heightError(self):
        """
        Test creating a Rectangle instance with height as a string.
        """
        with self.assertRaises(TypeError):
            Rectangle(43, "heightis2")

    def test_heightError2(self):
        """
        Test creating a Rectangle instance with height as a negative value.
        """
        with self.assertRaises(ValueError):
            Rectangle(43, -50)

    def test_xError(self):
        """
        Test creating a Rectangle instance with x-coordinate as a string.
        """
        with self.assertRaises(TypeError):
            Rectangle(3, 2, "Ex", 6)

    def test_xError2(self):
        """
        Test creating a Rectangle instance with x-coordinate as a negative
        value.
        """
        with self.assertRaises(ValueError):
            Rectangle(3, 2, -6, 6)

    def test_yError(self):
        """
        Test creating a Rectangle instance with y-coordinate as a string.
        """
        with self.assertRaises(TypeError):
            Rectangle(3, 2, 2, "trees")

    def test_yError2(self):
        """
        Test creating a Rectangle instance with y-coordinate as a negative
        value.
        """
        with self.assertRaises(ValueError):
            Rectangle(3, 2, 2, -3)

    def test_area(self):
        """
        Test calculating the area of a Rectangle.
        """
        rect3 = Rectangle(3, 3)
        self.assertEqual(rect3.area(), 9)


if __name__ == '__main__':
    unittest.main()
