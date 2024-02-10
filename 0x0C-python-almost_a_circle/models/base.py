#!/usr/python3
"""
Module: base.py

Description: This module features a base class.
"""


class Base:
    """
    Class Base: Represents a base class with an identifier.

    Instance Attribute:
    - id: An identifier.

    Class Attribute:
    - __nb__objects: Counter for objects.

    Methods:
    - __init__: Initializes the Base instance with an identifier.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes the Base instance with an identifier.

        Agrs:
        - id: An identifier.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
