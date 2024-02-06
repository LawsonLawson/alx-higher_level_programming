#!/usr/bin/python3
"""
Module: 2-append_write.py

Description: This module features a function that appends a string at the end
of a text file and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file.

    Agrs:
    - filename (string): The name of the file the text will be appended to.
    - text (string): The text to append at the end of the file.

    Returns: The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as opened_file:
        return (opened_file.write(text))
