#!/usr/bin/python3
"""
a class Square that defines a square
"""


class Square:
    """"
    A class square that has the ability to compute the area of the square
    given a valid size
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        return self.__size ** 2
