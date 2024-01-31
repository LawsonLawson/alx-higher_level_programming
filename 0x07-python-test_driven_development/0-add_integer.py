#!/usr/bin/python3
"""
This module features a function designed to calculate the sum of two numbers,
primarily focusing on integers while gracefully accommodating float values. In
cases where a float is provided as an argument, it undergoes conversion to an
integer before the operation is executed. It's crucial to note that this
conversion results in the loss of the decimal component, with only the integral
part contributing to the final output.
Beyond the specified argument types, the function diligently identifies and
handles unsupported inputs, raising errors when encountered.
"""


def add_integer(a, b=98):

    """
    Adds two integers and returns the result (integer).

    Args:
    - a (int or float): The first integer.
    - b (int or float): The second integer. Set to 98 by default.

    Returns:
    int: The sum of the two numbers, casted to an integer.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return (a + b)
