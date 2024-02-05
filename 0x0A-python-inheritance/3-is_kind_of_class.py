#!/usr/bin/python3
"""
Module: 3-kind_of_class

Description:
This module defines a function is_kind_of_class, which evaluates if an
object is of a specific class or a subclass of it.
Function:
is_kind_of_class(obj, a_class) - Takes an object and a class as agrs
"""


def is_kind_of_class(obj, a_class):
    """
    Function is_kind_of_class: Evaluates if an object is of a specified
    class or a subclass of it.

    Args:
    - obj: An object.
    - a_class: A class.
    Returns: True if the object is of the specified class or a subclass of
    it, False otherwise.
    """
    return isinstance(obj, a_class)
