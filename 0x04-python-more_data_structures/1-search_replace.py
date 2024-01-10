#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Replaces all occurences of 'search' with 'replace'in a given list.

    my_list : The input list to search and replace values.
    search: The value to be replaced.
    replace: The value to replace occurrences of 'search'.

    Returns: The modified list.
    """
    return [value if value != search else replace for value in my_list]
