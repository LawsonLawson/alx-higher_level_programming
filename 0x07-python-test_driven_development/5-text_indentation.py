#!/usr/bin/python3
"""
    This module features a text_indentation function which checks if input is
    valid and adds two new lines after any instances of `?`, `.` or `:`.
    Prints the result without spaces at the beginning or end of sentences.
"""


def text_indentation(text):
    """
    Prints the text with two new lines after each '.', '?' or ':'.
    When 'text is not a string, a TypeError is raised.

    Args:
    - text (str): The input string.
    """
    # Validate input
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Add two new lines after `?`, `.` or `:`
    new_text = "".join([x if x not in "?.:" else x + "\n\n" for x in text])

    # Remove spaces at the beginning or end of sentences and print the result
    print("\n".join([line.strip() for line in new_text.split("\n")]), end="")
