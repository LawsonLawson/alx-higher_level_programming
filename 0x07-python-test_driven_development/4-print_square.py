#!/usr/bin/python3
"""
This module features a functons that is designed to print a grid of '#' square.
The function takes an arg 'size' which determines the size of the square. Size
must be an integer and greater than or equal to 0, else an error will be thrown
.
"""


def print_square(size):
    """
    Prints a grid of '#' square with size 'size'

    Args:
        size (int): The size of the grid

    Returns:
        '#' grid of square.
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    elif isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
