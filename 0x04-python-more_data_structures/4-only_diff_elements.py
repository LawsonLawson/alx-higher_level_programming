#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    Returns a set of elements present in only one of two given sets.

    set_1: The first set.
    set_2: The second set.

    Returns: The set of elements unique to each set.
    """
    return set_1.symmetric_difference(set_2)
