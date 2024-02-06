#!/usr/bin/python3
"""
Module: 0-read_file.py

Description: This module defines a function read_file that reads a file and
prints its content to the console.
"""


def read_file(filename=""):
    """
    This function reads a file and prints the contents of the file to sdout.

    Args:
    - filename (string): The name of the file
    """
    with open(filename, encoding="utf-8") as file_content:
        print(file_content.read(), end='')
