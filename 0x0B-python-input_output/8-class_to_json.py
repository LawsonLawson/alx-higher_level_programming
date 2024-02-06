#!/usr/bin/python3
"""
Module: 8-class_to_json.py

Description: This module features a function that returns the dictionary
description with a simple data structure.
"""


def class_to_json(obj):
    """
    Converts an object's attributes to a JSON serializable dictionary.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("obj must be an instance of a class")

    json_dict = {}
    for attr, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[attr] = value
        else:
            raise TypeError(f"Attribute '{attr}' of type "
                            f"'{type(value).__name__}' is not serializable")

    return json_dict
