#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Adds unique integers from a list , ensuring each is worked on once.

    my_list: The input list of integers.

    Returns: The sum of unique integers.
    """
    if my_list is None:
        my_list = []
    unique_sum = sum(set(my_list))
    return unique_sum
