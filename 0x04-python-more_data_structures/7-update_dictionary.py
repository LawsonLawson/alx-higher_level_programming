#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    Replaces a key-value pair in dictionary.

    a_dictionary: The input dictionary.
    key: The key to be replaced.
    value: The value in line with the key.

    Returns: The updated dictionary.
    """
    a_dictionary[key] = value
    return a_dictionary
