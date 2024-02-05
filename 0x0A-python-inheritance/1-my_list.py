#!/usr/bin/python3
"""
Module: 1-my_list

Description:
This module defines the class MyList, which inherits from the list class.
The class assumes that all elements in the list are integers.

Class:
MyList - Inherits from the list class and includes a method print_sorted()
to print the list in sorted order.
"""


class MyList(list):
    """
    Class MyList: Inherits from the list class and assumes all elements in the
    list are integers.

    Methods:
    print_sorted() - Prints the list in sorted order.
    """
    def print_sorted(self):
        """Print the list in sorted order."""
        sorted_list = sorted(self)
        formatted_elements = [f"{element:d}" for element in sorted_list]
        print("[" + ", ".join(formatted_elements) + "]")
