#!/usr/bin/python3
"""
a class Square that defines a square
"""


class Square:
    """"
    Attributes:
    __size: the size of the square
    value: the setter property
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif 0 > value:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        for i in range(self.__size):
            for j in range(self.__size):
                print('{}'.format('#'), end='')
            print()
        if self.size == 0:
            print()
