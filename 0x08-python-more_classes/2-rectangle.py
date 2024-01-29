#!/usr/bin/python3
"""
A module that features a blueprint for a rectangle
"""


class Rectangle:
    """
    Rectangle blueprint

    Agrs:
    - widht (int): The width of the rectangle. (default set to 0)
    - height (int): The height of the rectangle. (default set to 0)
    """
    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError('width must be >= 0')
        elif not isinstance(height, int):
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be >= 0')
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        _area = self.__height * self.__width
        return _area

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        _perimeter = (self.__height + self.__width) * 2
        return _perimeter
