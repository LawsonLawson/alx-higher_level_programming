#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    Deletes a key form a dictionary.

    a_dictionary: The input dictionary.
    key: The key to be deleted. Defaults to an empty string.

    Return: The updated dictionary after deletion.
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
