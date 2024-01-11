#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    """Returns a new matrix with each element squared."""
    return [list(map(lambda x: x**2, row)) for row in matrix]
