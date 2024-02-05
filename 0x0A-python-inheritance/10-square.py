#!/usr/bin/python3
"""
Module: 10-square

Description:
This module defines the class Square, a subclass of Rectangle. The Square
class has an instance attribute 'size' and inherits methods from its superclass
Rectangle.

Classes:
- Rectangle: Class with methods for a rectangle.
- Square: Subclass of Rectangle with an instance attribute 'size'.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class Square: Subclass of Rectangle with an instance attribute 'size'.

    Instance Attributes:
    - size: An integer >= 0.

    Methods:
    - __init__: Instantiates a square with a given size.
    """
    def __init__(self, size):
        """
        Initializes a square with a given size.

        Arguments:
        - size: Must be an integer >= 0.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
