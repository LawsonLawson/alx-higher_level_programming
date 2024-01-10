#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    Prints a dictionary with keys sorted in ascending order.

    a_dictionary: The input dictionary.

    Returns: None (sorted returns none)
    """
    for key in sorted(a_dictionary):
        print("{}: {}".format(key, a_dictionary[key]))
