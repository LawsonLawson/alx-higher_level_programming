#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Prints all integers of a list in reverse order"""
    my_list_copy = my_list.copy()
    my_list_copy.reverse()
    for integers in my_list_copy:
        print('{:d}'.format(integers))
