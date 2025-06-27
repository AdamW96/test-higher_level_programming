#!/usr/bin/python3
"""
This module provides a function to add two integers.

The function handles type checking and conversion from float to int.
It validates inputs and raises appropriate exceptions for invalid types.
"""


def add_integer(a, b=98):
    """
    Adds two integers after validation and type conversion.

    This function takes two parameters that must be integers or floats.
    Float values are cast to integers before addition.

    Args:
        a: First number (must be int or float)
        b: Second number (must be int or float), defaults to 98

    Returns:
        int: The sum of a and b as integers

    Raises:
        TypeError: If a is not an integer or float
        TypeError: If b is not an integer or float
    """
    # Check type of 'a'
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    # Check type of 'b'
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Try to convert to integers, catch overflow/value errors
    try:
        a_int = int(a)
    except (OverflowError, ValueError):
        raise TypeError("a must be an integer")

    try:
        b_int = int(b)
    except (OverflowError, ValueError):
        raise TypeError("b must be an integer")

    return a_int + b_int
