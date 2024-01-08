#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Prints all integers of a list in reverse order"""
    if my_list:
        my_list.reverse()
        for integers in range(len(my_list)):
            print('{:d}'.format(my_list[integers]))
