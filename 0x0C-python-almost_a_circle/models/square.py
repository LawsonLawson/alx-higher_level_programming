#!/usr/bin/python3

"""
Module: square.py

Description: This module features a class 'Square' that inherits from the
'Rectangle' class.
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square: Represents a square, inherits from Rectangle.

    Inherits from:
    - Rectangle: A class representing a rectangle.

    Instance Attributes:
    - size: Size of the square.

    Methods:
    - __init__: Initializes the Square instance with size, x, y, and an
    identifier.
    - __str__: Returns a string representation of the Square instance.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes the Square instance with size, x, y, and an identifier.

        Args:
        - size: Size of the square.
        - x: X coordinate of the square. (Default: 0)
        - y: Y coordinate of the square. (Default: 0)
        - id: Identifier of the square. (Default: None)
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a string representation of the Square object.

        Returns:
        - String representation of the square instance.
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

    @property
    def size(self):
        """Getter for size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size."""
        self.width = value
        self.height = value
