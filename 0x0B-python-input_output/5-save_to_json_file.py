#!/usr/bin/python3
"""
Module: 5-save_to_json_file.py

Description: This module features a function that writes an Object to a text
file using JSON representation.
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file using JSON representation.

    Args:
    - my_obj : The object
    - filename : The file to write to
    """
    with open(filename, "w", encoding="utf-8") as opened_file:
        obj = json.dumps(my_obj)
        return opened_file.write(obj)
