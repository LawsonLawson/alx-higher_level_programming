#!/usr/bin/python3
"""
This module features a function designed to calculate the sum of two numbers,
primarily focusing on integers while gracefully accommodating float values. In
cases where a float is provided as an argument, it undergoes conversion to an
integer before the operation is executed.
"""


def add_integer(a, b=98):

    """Adds two integers and returns the result (integer).
    Returns: int: The sum of the two numbers, casted to an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return_value = a + b
    return return_value
