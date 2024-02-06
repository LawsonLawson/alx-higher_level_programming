#!/usr/bin/python3
"""
Module: 1-write_file.py

Description: This module defines a function write_file which is responsible for
writing a characters into a text file.
"""


def write_file(filename="", text=""):
    """
    Writes numbers of given characters into a file and returns the number
    of characters written.

    Args:
    - filename (string): The name of the file to be written into.
    - text (string): The text or say characters to write into the file.

    Return: The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as opened_file:
        return (opened_file.write(text))
