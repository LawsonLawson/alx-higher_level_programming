#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers of a matrix.
    """
    new_list = matrix[:]

    def squared(nums):
        return [element ** 2 for element in nums]
    squared_matrix = list(map(squared, new_list))
    return squared_matrix
