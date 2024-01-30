#!/usr/bin/python3
"""
LockedClass Module

Defines the LockedClass, which restricts dynamic creation of new instance
attributes, except for 'first_name'.
"""


class LockedClass:
    """
    A class that restricts the dynamic creation of new instance attributes,
    allowing only the attribute 'first_name'.
    """
    __slots__ = ["first_name"]
