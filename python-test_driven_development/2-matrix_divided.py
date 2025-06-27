#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix.

The function performs validation and returns a new matrix with divided values.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number.

    Args:
        matrix: List of lists containing integers or floats
        div: Number to divide by (int or float)

    Returns:
        list: New matrix with all elements divided by div,
            rounded to 2 decimal places

    Raises:
        TypeError: If matrix is not a list of lists of numbers,
                or if div is not a number
        ZeroDivisionError: If div is 0
    """
    # Check if matrix is a list
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if each element is a list of numbers and same size
    row_length = None
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )

        if len(row) == 0:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )

        if row_length is None:
            row_length = len(row)
        elif len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
                )

    # Check div
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Create new matrix
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)

    return new_matrix
