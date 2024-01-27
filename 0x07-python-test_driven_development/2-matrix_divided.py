#!/usr/bin/ptyhon3
"""
This modules features the matrix_divided function. It returns the result
of the division of all elements in a given matrix by a divisor 'di'.
It accepts integers and floating point numbers, any data type outiside of
this scope will throw and error.
"""


def matrix_divided(matrix, div):
    """
    Divides elements of a given matrix by 'div'.

    Args:
        matrix (list): The matrix to divide.
        div (int, float): The divisor.

    Returns:
        A matrix with all elements divided by the divisor (div).
    """
    def validate_matrix_structure(matrix):
        if not isinstance(matrix, list) or not matrix \
                or not all(isinstance(row, list) for row in matrix) \
                or not all(isinstance(element, (int, float)) for row in matrix
                           for element in row):
            raise TypeError("matrix must be a matrix (list of lists) of "
                            "integers/floats")

    def validate_row_sizes(matrix):
        if any(len(row) != len(matrix[0]) for row in matrix[1:]):
            raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number and not zero
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Validate the matrix structure
    validate_matrix_structure(matrix)

    # Check if all rows have the same size
    validate_row_sizes(matrix)

    # Check if the matrix is empty
    if not matrix[0]:
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    # Perform matrix division
    result_matrix = [[round(element / div, 2) for element in row]
                     for row in matrix]

    return result_matrix
