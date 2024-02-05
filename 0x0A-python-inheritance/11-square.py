#!/usr/bin/python3
"""
Module: base_geometry

Description:
This module defines the classes BaseGeometry, Rectangle, and Square.
BaseGeometry serves as a base class with methods 'area()' and
'integer_validator()' for validating integers. Rectangle is a subclass
of BaseGeometry with private attributes 'width' and 'height', while Square is
a subclass of Rectangle with an additional private attribute 'size'.

Classes:
- BaseGeometry: Base class with methods 'area()' and 'integer_validator()'.
- Rectangle: Subclass of BaseGeometry with private attributes 'width' and
'height'.
- Square: Subclass of Rectangle with an additional private attribute 'size'.
"""


class BaseGeometry:
    """
    Class BaseGeometry: Base class with methods 'area()' and
    'integer_validator()'.

    Methods:
    - area: Returns the area; raises an exception if not implemented.
    - integer_validator: Validates the value for being an integer and greater
    than 0.
    """
    def area(self):
        """
        Returns the area.

        Raises:
        - Exception: If not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value for being an integer and greater than 0.

        Arguments:
        - name: A name (string).
        - value: Should be an integer.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Class Rectangle: Subclass of BaseGeometry with private attributes 'width'
    and 'height'.

    Instance Attributes:
    - width: Private attribute, must be a positive integer.
    - height: Private attribute, must be a positive integer.

    Methods:
    - __init__: Initializes the Rectangle class with width and height.
    - __str__: Returns a string representation of the Rectangle.
    - area: Returns the area of the Rectangle.
    """
    def __init__(self, width, height):
        """
        Initializes the Rectangle class with width and height.

        Arguments:
        - width: Must be a positive integer.
        - height: Must be a positive integer.
        """
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Returns a string representation of the Rectangle.
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

    def area(self):
        """
        Returns the area of the Rectangle.
        """
        return self.__width * self.__height


class Square(Rectangle):
    """
    Class Square: Subclass of Rectangle with an additional private attribute
    'size'.

    Instance Attributes:
    - size: Private attribute, must be a positive integer.

    Methods:
    - __init__: Initializes the Square class with a given size.
    - __str__: Returns a string representation of the Square.
    """
    def __init__(self, size):
        """
        Initializes the Square class with a given size.

        Arguments:
        - size: Must be a positive integer.
        """
        BaseGeometry.integer_validator(self, "size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size

    def __str__(self):
        """
        Returns a string representation of the Square.
        """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
