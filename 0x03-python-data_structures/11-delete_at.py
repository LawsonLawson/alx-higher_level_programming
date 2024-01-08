#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    Deletes the item at a specified position in a list
    """
    bounds = len(my_list)
    if my_list:
        if idx < 0:
            return my_list
        elif idx >= bounds:
            return my_list
        elif my_list is None:
            return my_list
        else:
            del my_list[idx]
        return my_list
