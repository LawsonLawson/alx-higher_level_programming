#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    Deletes the item at a specified position in a list
    """
    bounds = len(my_list)
    if my_list and 0 <= idx < bounds:
        del my_list[idx]
    return my_list
