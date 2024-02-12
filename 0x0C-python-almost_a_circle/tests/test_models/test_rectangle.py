#!/usr/bin/python3


"""
Module: test_rectangle.py

Desctiption: This module features a unittest for the "Rectangle" class.
"""


import unittest
import io
from contextlib import redirect_stdout
from models.base import Base
import sys
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

    def test_floatWidthHeight(self):
        """
        Test creating a Rectangle instance with floating-point width and
        height.
        This should raise a TypeError.
        """
        with self.assertRaises(TypeError):
            Rectangle(3.5, 4.7)

    def test_zeroWidth(self):
        """
        Test creating a Rectangle instance with zero width.
        This should raise a ValueError.
        """
        with self.assertRaises(ValueError):
            Rectangle(0, 4)

    def test_zeroHeight(self):
        """
        Test creating a Rectangle instance with zero height.
        This should raise a ValueError.
        """
        with self.assertRaises(ValueError):
            Rectangle(3, 0)

    def test_negativeWidthHeight(self):
        """
        Test creating a Rectangle instance with negative width and height.
        This should raise a ValueError.
        """
        with self.assertRaises(ValueError):
            Rectangle(-3, -4)

    def test_largeWidthHeight(self):
        """
        Test creating a Rectangle instance with extremely large width and
        height values.
        """
        rect = Rectangle(999999999999, 999999999999)
        self.assertEqual(rect.width, 999999999999)
        self.assertEqual(rect.height, 999999999999)

    def test_updateKwargs(self):
        """
        Test updating the attributes of a Rectangle using **kwargs.
        """
        rect = Rectangle(3, 4, 5, 6, 7)
        rect.update(width=8, height=9, x=10, y=11, id=12)
        self.assertEqual(str(rect), "[Rectangle] (12) 10/11 - 8/9")

    def test_updateInvalidArgs(self):
        """
        Test the behavior when passing invalid arguments to the update method.
        """
        rect = Rectangle(3, 4, 5, 6, 7)
        with self.assertRaises(TypeError):
            rect.update("invalid", "arguments")

    def test_updatePartialArgs(self):
        """
        Test updating the attributes of a Rectangle with only some arguments
        provided.
        """
        rect = Rectangle(3, 4, 5, 6, 7)
        rect.update(8, 9)
        self.assertEqual(str(rect), "[Rectangle] (8) 5/6 - 9/4")

    def test_toDictionary(self):
        """
        Test the to_dictionary method to ensure it returns the expected
        dictionary representation.
        """
        rect = Rectangle(3, 4, 5, 6, 7)
        rect_dict = rect.to_dictionary()
        expected_dict = {'id': 7, 'width': 3, 'height': 4, 'x': 5, 'y': 6}
        self.assertEqual(rect_dict, expected_dict)

    def test_createNegativeX(self):
        """
        Test creating a Rectangle instance with negative x-coordinate.
        This should raise a ValueError.
        """
        with self.assertRaises(ValueError):
            Rectangle(3, 4, -5, 6, 7)

    def test_createNegativeY(self):
        """
        Test creating a Rectangle instance with negative y-coordinate.
        This should raise a ValueError.
        """
        with self.assertRaises(ValueError):
            Rectangle(3, 4, 5, -6, 7)

    def test_width_invalid_type(self):
        """
        Test setting width with an invalid type.
        """
        with self.assertRaises(TypeError) as context:
            Rectangle("invalid", 2)
        self.assertEqual(str(context.exception), "width must be an integer")

    def test_width_negative_value(self):
        """
        Test setting width with a negative value.
        """
        with self.assertRaises(ValueError) as context:
            Rectangle(-5, 2)
        self.assertEqual(str(context.exception), "width must be > 0")

    def test_height_invalid_type(self):
        """
        Test setting height with an invalid type.
        """
        with self.assertRaises(TypeError) as context:
            Rectangle(10, "invalid")
        self.assertEqual(str(context.exception), "height must be an integer")

    def test_height_zero_value(self):
        """
        Test setting height with a zero value.
        """
        with self.assertRaises(ValueError) as context:
            Rectangle(10, 0)
        self.assertEqual(str(context.exception), "height must be > 0")

    def test_x_invalid_type(self):
        """
        Test setting x with an invalid type.
        """
        with self.assertRaises(TypeError) as context:
            Rectangle(10, 5, "invalid")
        self.assertEqual(str(context.exception), "x must be an integer")

    def test_y_invalid_type(self):
        """
        Test setting y with an invalid type.
        """
        with self.assertRaises(TypeError) as context:
            Rectangle(10, 5, 3, "invalid")
        self.assertEqual(str(context.exception), "y must be an integer")

    def test_y_negative_value(self):
        """
        Test setting y with a negative value.
        """
        with self.assertRaises(ValueError) as context:
            Rectangle(10, 5, 3, -2)
        self.assertEqual(str(context.exception), "y must be >= 0")

    def test_invalid_width_height(self):
        """Test for invalid width and height values during instantiation."""
        with self.assertRaises(ValueError):
            Rectangle(-10, 5)
        with self.assertRaises(ValueError):
            Rectangle(10, -5)

    def test_invalid_x_y(self):
        """Test for invalid x and y values during instantiation."""
        with self.assertRaises(ValueError):
            Rectangle(10, 5, -2, 3)
        with self.assertRaises(ValueError):
            Rectangle(10, 5, 2, -3)

    def test_save_to_file_empty_list(self):
        """Test saving an empty list of rectangles to file."""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_from_json_string_empty_string(self):
        """Test loading from an empty JSON string."""
        self.assertEqual(Rectangle.from_json_string(""), [])

    def test_load_from_file_nonexistent_file(self):
        """Test loading from a nonexistent file."""
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_display_different_sizes(self):
        """
        Test display method with rectangles of different sizes.
        """
        r1 = Rectangle(2, 3, 0, 0, 1)
        expected_output = "##\n##\n##\n"
        with io.StringIO() as buffer, redirect_stdout(buffer):
            r1.display()
            output = buffer.getvalue()
            self.assertEqual(output, expected_output)

    def test_set_to_max_width(self):
        """
        Tests setting the width attribute to the maximum allowed integer value.
        """
        r = Rectangle(2, 3)
        r.width = sys.maxsize
        self.assertEqual(r.width, sys.maxsize)

    def test_set_to_max_height(self):
        """
        Tests setting the height attribute to the maximum allowed integer value
        """
        r = Rectangle(2, 3)
        r.height = sys.maxsize
        self.assertEqual(r.height, sys.maxsize)

    def test_set_to_max_x(self):
        """
        Tests setting the x attribute to the maximum allowed integer value.
        """
        r = Rectangle(2, 3)
        r.x = sys.maxsize
        self.assertEqual(r.x, sys.maxsize)

    def test_set_to_max_y(self):
        """
        Tests setting the y attribute to the maximum allowed integer value.
        """
        r = Rectangle(2, 3)
        r.y = sys.maxsize
        self.assertEqual(r.y, sys.maxsize)


if __name__ == '__main__':
    unittest.main()
