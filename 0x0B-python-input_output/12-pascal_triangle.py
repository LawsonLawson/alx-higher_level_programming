#!/usr/bin/python3
"""
Module: 12-pascal_triangle.py

Description: Returns a list of lists of integers representing the Pascal’s
triangle.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal’s triangle of n.

    Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    my_triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(my_triangle[i - 1][j - 1] + my_triangle[i - 1][j])
        row.append(1)
        my_triangle.append(row)

    return my_triangle
