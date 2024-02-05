#!/usr/bin/python3
"""
Module: 8-rectangle

Description:
This module defines the class Rectangle, which is a subclass of BaseGeometry.
The Rectangle class has private instance attributes 'width' and 'height', and
it ensures that both are positive integers during instantiation.

Class:
Rectangle - Subclass of BaseGeometry with private attributes 'width' and
'height'.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class Rectangle: Subclass of BaseGeometry with private attributes 'width'
    and 'height'.

    Instance Attributes:
    - width: Private attribute, must be a positive integer.
    - height: Private attribute, must be a positive integer.
    """

    def __init__(self, width, height):
        """
        Instantiates a Rectangle if width and height are positive integers.

        Arguments:
            width: Must be a positive integer.
            height: Must be a positive integer.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
