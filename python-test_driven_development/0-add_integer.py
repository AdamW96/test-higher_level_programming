#!/usr/bin/python3
"""
This module provides a function to add two integers.

The function handles type checking and conversion from float to int.
"""
def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a: First number (int or float)
        b: Second number (int or float), defaults to 98

    Returns:
        int: The sum of a and b

    Raises:
        TypeError: If a or b is not an integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Handle float('nan') and float('inf')
    if a != a or a == float('inf') or a == float('-inf'):
        raise ValueError("cannot convert float NaN to integer")
    if b != b or b == float('inf') or b == float('-inf'):
        raise ValueError("cannot convert float NaN to integer")

    return int(a) + int(b)
