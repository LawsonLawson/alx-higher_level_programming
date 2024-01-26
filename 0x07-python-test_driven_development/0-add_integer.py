#!/usr/bin/python3
"""A function that adds 2 integers"""

def add_integer(a, b=98):
    """
    Adds two integers and returns the result (integer).

    Args:
    - a (int or float): The first integer.
    - b (int or float): The second integer. Set to 98 by default.

    Returns:
    int: The sum of the two numbers, casted to an integer.
    """
    if not (isinstance(a, (int, float))):
        raise TypeError('a must be an integer')
    a = int(a)
    if not (isinstance(b, (int, float))):
        raise TypeError('b must be an integer')
    b = int(b)

    return a + b
