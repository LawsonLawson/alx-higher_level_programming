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
    - save_to_file: Write the JSON string representation of list_objs to a
    file.
    - from_json_string: Returns the list of dictionaries from the JSON string
    representation.
    - create: Returns an object with all attributes already set.
    - load_from_file: Returns a list of objects.
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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string representation of list_objs to a file.

        Args:
        - list_objs: List of objects inheriting from Base.
        """
        file = cls.__name__ + '.json'
        with open(file, 'w') as opened_file:
            if list_objs is None:
                opened_file.write('[]')
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                opened_file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of directories from the JSON string representation.

        Args:
        - json_string: String representing a list of dictionaries.

        Returns:
        - List of dictionaries.
        """
        if json_string is None or json_string == '':
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set.

        Args:
        - **dictionary: Double pointer to a dictionary.

        Returns:
        - Objects with all attributes already set.
        """
        if cls.__name__ == 'Rectangle':
            tryout = cls(1, 1)
        elif cls.__name__ == 'Square':
            tryout = cls(1)
        else:
            raise TypeError('Unsupported class')
        tryout.update(**dictionary)
        return tryout

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of objects from a JSON file.

        Returns:
        - List of objects.
        """
        file = cls.__name__ + '.json'
        try:
            with open(file, 'r') as opened_file:
                j_data = opened_file.read()
                d_list = cls.from_json_string(j_data)
                obj_list = [cls.create(**i) for i in d_list]
                return obj_list
        except FileNotFoundError:
            return []
