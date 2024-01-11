#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """
    Multiplies each element in a list by a specified number using the map
    function.

    my_list: The input list. Defaults to an empty list.
    number: The multiplier. Defaults to 0.

    Returns: A new list with elements multiplied by the specified number.
    """
    if my_list is None:
        my_listt = []
    return list(map(lambda x: x * number, my_list))
