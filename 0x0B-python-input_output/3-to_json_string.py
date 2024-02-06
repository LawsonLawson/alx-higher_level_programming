#!/usr/bin/python3
"""
Module: 3-to_json_string.py

Description: This module features a function that returns the JSON
representation of an object.
"""

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object.

    Args:
    - my_obj (string): The object.
    """
    return (json.dumps(my_obj))
