#!/usr/bin/python3
"""
Module: 6-load_from_json_file.py

Description: This module features a function that creates an Object from a
"JSON file".
"""

import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file

    Agrs:
    - filename (string): The name of the file
    """
    with open(filename, "r", encoding="utf-8") as opened_file:
        obj = opened_file.read()
        return (json.loads(obj))
