#!/usr/python3
"""
Module: base.py

Description: This module features a base class.
"""

import json


class Base:
    """
    Class Base: Represents a base class with an identifier.

    Methods:
    - __init__: Initializes the Base instance with an identifier.
    - to_json_string: Returns the JSON string representation of a list of
    dictionaries.
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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.

        Args:
        - list_dictionaries: List of dictionaries.

        Returns:
        - JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        else:
            return json.dumps(list_dictionaries)
