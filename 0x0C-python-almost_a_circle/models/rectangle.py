#!/usr/bin/python3

""""
Module: rectangle.py

Description: This module features a class 'Rectangle' that inherits from the
'Base' class
"""

from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle: Represents a rectangle with width, height, x, y, and an
    identifier.

    Inherits from:
    - Base: A base class with an identifier.

    Instance Attributes:
    - width: Width of the rectangle.
    - height: Height of the rectangle.
    - x: X coordinate of the rectangle.
    - y: Y coordinate of the rectangle.

    Methods:
    - __init__: Initializes the Rectangle instance with width, height, x, y,
    and an identifier.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes the Rectangle instance with width, height, x, y, and an
        identifier.

        Args:
        - width: Width of the rectangle.
        - height: Height of the rectangle.
        - x: X coordinate of the rectangle. (Default: 0)
        - y: Y coordinate of the rectangle. (Default: 0)
        - id: Identifier of the rectangle. (Default: None)
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width."""
        self.__width = value

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height."""
        self.__height = value

    @property
    def x(self):
        """Getter for x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x."""
        self.__x = value

    @property
    def y(self):
        """Getter for y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y."""
        self.__y = value
