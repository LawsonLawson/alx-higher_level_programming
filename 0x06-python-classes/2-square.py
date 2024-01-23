#!/usr/bin/python3
"""
a class Square that defines a square by: (based on 1-square.py) with instance
attribute 'size' and instantiation with optional size:
    def __init__(self, size=0)
"""


class Square:
    """"
    A class square
    .. I am still building this one, it is not a complete class yet
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif 0 > size:
            raise ValueError('size must be >=0')
        else:
            self.__size = size
