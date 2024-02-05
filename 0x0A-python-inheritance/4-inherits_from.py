#!/usr/bin/python3
"""
Module: inherits_from

Description:
This module defines a function inherits_from, which evaluates if an object
is strictly from a subclass of a specified class.

Function:
inherits_from(obj, a_class) - Takes an object and a class as args, returning
True if the object is from a subclass of the specified class (excluding the
class itself); otherwise, it returns False.
"""


def inherits_from(obj, a_class):
    """
    Function inherits_from: Evaluates if an object is strictly from a subclass
    of a specified class.

    Args:
    - obj: An object.
    - a_class: A class.

    Returns:
    True if the obj is from a subclass of a_class excluding a_class, False
    otherwise.
    """
    return (issubclass(type(obj), a_class) and (type(obj) is not a_class))
