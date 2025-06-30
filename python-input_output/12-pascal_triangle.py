#!/usr/bin/python3
"""
This module provides a function to generate Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    Return a list of lists of integers representing Pascal's triangle of n.

    Pascal's triangle is constructed where each number is the sum of the two
    numbers directly above it. The triangle starts with 1 at the top.

    Args:
        n (int): The number of rows in Pascal's triangle

    Returns:
        list: List of lists representing Pascal's triangle, empty if n <= 0
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        # Start each row with 1
        row = [1]

        # Calculate middle elements (if any)
        if i > 0:
            for j in range(1, i):
                # Each element is sum of two elements above it
                element = triangle[i - 1][j - 1] + triangle[i - 1][j]
                row.append(element)

            # End each row with 1 (except the first row)
            row.append(1)

        triangle.append(row)

    return triangle
