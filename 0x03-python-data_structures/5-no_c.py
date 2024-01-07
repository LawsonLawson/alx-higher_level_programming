#!/bin/usr/python3
def no_c(my_string):
    """
    Removes all 'C' and 'c' characters from a string
    """
    new_string = ''.join(char for char in my_string if char.lower() != 'c')
    return new_string
