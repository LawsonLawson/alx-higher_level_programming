#!/usr/bin/python3
def max_integer(my_list=[]):
    """
    Finds the biggest integer of a list
    """
    if my_list == '' or my_list is None:
        return None
    my_list.sort()
    return my_list[-1]
