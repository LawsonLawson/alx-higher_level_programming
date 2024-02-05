#!/usr/bin/python3
"""
This is a module that features the 0-lookup
"""


def lookup(obj):
    """
    This function lists all the available methods of an object and attributes.

    Args:
    - obj: The object.

    Returns: A list.
    """
    return dir(obj)
