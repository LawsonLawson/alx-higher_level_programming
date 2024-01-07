#!/usr/bin/python3
def element_at(my_list, idx):
    """Retrives an element from a list like in C"""
    for elements in my_list:
        if idx < 0:
            return None
        elif idx >= len(my_list):
            return None
        else:
            return my_list[idx]
