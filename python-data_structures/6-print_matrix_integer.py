#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers.

    Args:
        matrix: A 2D list of integers to print
    """
    for row in matrix:
        for i, integer in enumerate(row):
            if i > 0:
                print(" ", end="")
            print("{:d}".format(integer), end="")
        print()
