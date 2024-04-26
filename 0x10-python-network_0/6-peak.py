#!/usr/bin/python3
"""
This script finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.

    Parameters:
        list_of_integers (list): List of integers to find the peak of.

    Returns:
        int or None: The peak of the list of integers, or None should the
        list be empty.
    """
    size = len(list_of_integers)

    # Check if the list is empty
    if size == 0:
        return None

    # Otherwise ... sort the list in ascending order
    list_of_integers.sort()

    # Return the last element, which is the peak
    return list_of_integers[-1]
