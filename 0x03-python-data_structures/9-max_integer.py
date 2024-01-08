#!/usr/bin/python3
def max_integer(my_list=[]):
    """
    Finds the biggest integer of a list
    """
    if my_list == '' or len(my_list) == 0:
        return None
    my_list.sort()
    return my_list[-1]
