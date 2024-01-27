#!/usr/bin/python3
"""
This module features a function that prints a simple message to sdout. It takes
2 args which are supposed to be strings else a TypeError will be raised, prints
the string 'My name is .... .... ' and substitutes the args which are first and
and last names into the string.
"""


def say_my_name(first_name, last_name=""):

    """
    Prints a the string 'My name is bla bla' to stdout.

    Agrs:
        fist_name (str): The first name of the user.
        last_name (str): The last name of the user.

    Returns:
        A formatted string 'My name is <> <> ' to stdou.
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    elif not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    else:
        print(f'My name is {first_name} {last_name}')
