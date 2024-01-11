#!/usr/bin/python3
def best_score(a_dictionary):
    """
    Returns the key with the highest integer value in a given dictionary.

    a_dictionary: The input dictionary.

    Returns: The key with the highest value or None if the dictionary is empty.
    """
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)
