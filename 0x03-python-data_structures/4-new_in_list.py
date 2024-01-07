#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replaces an element of a list at a specified position without
    modifying the orginal"""
    for elements in my_list:
        if idx < 0:
            return my_list
        elif idx >= len(my_list):
            return my_list
        else:
            new_list = my_list.copy()
            new_list[idx] = element
            return new_list
