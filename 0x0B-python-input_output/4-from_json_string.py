#!/usr/bin/python3
"""
Module: 4-from_json_string.py

Description: This module features a function that returns the JSON
representation of an object (Python data structure).
"""

import json


def from_json_string(my_str):
    """
    Returns the JSON representation of an object (Python data structure).

    Args:
    - my_str
    """
    return (json.loads(my_str))
