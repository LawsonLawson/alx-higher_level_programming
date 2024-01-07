#!/usr/bin/python3
def max_integer(my_list=[]):
    """
    Finds the biggest integer of a list
    """
    if len(my_list) == 0:
        return None
    if my_list == '':
        return
    max_integer = my_list[0]
    for integer in my_list:
        if integer > max_integer:
            max_integer = integer
            return max_integer
