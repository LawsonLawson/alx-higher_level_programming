#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    Prints a matrix of integers
    """
    if matrix:
        for row in matrix:
            for column in row:
                print('{:d}'.format(column), end='')
                if row.index(column) != len(row) - 1:
                    print(' ', end='')
            print('')
