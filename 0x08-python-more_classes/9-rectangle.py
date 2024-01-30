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

    number_of_instances = 0
    print_symbol = '#'

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
            return ('\n'.join([''.join([str(self.print_symbol)
                               for w in range(self.__width)])
                               for h in range(self.__height)]))

    def __repr__(self):
        return ('Rectangle(' + '{:d}'.format(self.__width) + ', ' +
                '{:d}'.format(self.__height) + ')')

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')
        elif type(rect_2) is not Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')
        return (rect_1 if rect_1.area() >= rect_2.area() else rect_2)

    @classmethod
    def square(cls, size=0):
        return (Rectangle(size, size))

    def change_symbol(sym):
        type(self).print_symbol = sym

    def area(self):
        _area = self.__height * self.__width
        return _area

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        _perimeter = (self.__height + self.__width) * 2
        return _perimeter
