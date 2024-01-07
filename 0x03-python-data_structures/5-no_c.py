#!/bin/usr/python3
def no_c(my_string):
    """
    Removes all 'C' and 'c' characters from a string
    """
    if my_string:
        new_string = ''
        for char in my_string:
            if char != 'c' and char != 'C':
                new_string += char
        return new_string
    else:
        return my_string
