#!/usr/bin/python3
"""
Module: 2-is_same_class.

Description:
    This module defines the function is_same_class, which evaluates if an
    object belongs to a specific class exactly.

Function:
    is_same_class(obj, a_class) - Takes an object and a class as args while
    returning either true if the object type matches the class or false if not.
"""


def is_same_class(obj, a_class):
    """
    Function is_same_class: Evaluates if an object belongs a specified class.

    Args:
        obj: An object
        a_class: A class

    Return:
        True if the object type matches the class exactly, False otherwise
    """
    return (type(obj)) == a_class
