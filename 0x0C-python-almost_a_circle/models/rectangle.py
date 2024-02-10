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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """
        Returns a string representation of the Rectangle object.

        Returns:
        - String representation of the rectangle instance.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height
                )

    def area(self):
        """
        Computes and returns the area of the rectangle.

        Returns:
        - A value (int): Area of the rectangle.
        """
        return (self.width * self.height)

    def display(self):
        """
        Prints the Rectangle instance with the '#' character considering
        coordinates x and y.
        """
        for i in range(self.y):
            print()
        for j in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def update(self, *args, **kwargs):
        """
        Assigns key/value args to attributes in of the object.

        Args:
        - *args: Positional arguments.
        - **kwargs: Keyword arguments.
        """
        if args:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
            else:
                for key, value in kwargs.items():
                    setattr(self, key, value)

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """Getter for x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x."""
        if not isinstance(value, int):
            raise TypeError("x must be an interger")
        if value < 0:
            raise ValueError("y must >= 0")

        self.__x = value

    @property
    def y(self):
        """Getter for y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value
