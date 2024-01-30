#!/usr/bin/python3
"""
A module that features a blueprint for a rectangle
"""


class Rectangle:
    number_of_instances = 0
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
        Rectangle.number_of_instances += 1

    def __str__(self):
        if self.__width > 0 and self.__height > 0:
            return ('\n'.join([''.join(['#'for w in range(self.__width)])
                               for h in range(self.__height)]))
        else:
            return ''

    def __repr__(self):
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

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
