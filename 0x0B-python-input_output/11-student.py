#!/usr/bin/python3
"""
Module: 11-student.py

Description: This module features a class which is a built upon class from
the class in 10-student module.
"""


class Student:
    """
    Defines a student with first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with first name, last name, and
        age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        If attrs is None, retrieves all attributes. Otherwise, retrieves only
        the attributes specified in the attrs list.
        """
        if attrs is None:
            return self.__dict__
        json_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                json_dict[attr] = getattr(self, attr)
        return json_dict

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with values from a
        dictionary.

        Assumes json is a dictionary where each key is a public attribute name
        and each value is the value of the corresponding attribute.
        """
        for key, value in json.items():
            setattr(self, key, value)
