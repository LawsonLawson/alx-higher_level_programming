#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    Deletes the item at a specified position in a list
    """
    if my_list:
        if idx < 0:
            return my_list
        else:
            del my_list[idx]
        return my_list
