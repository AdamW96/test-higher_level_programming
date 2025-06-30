#!/usr/bin/python3
"""
This module provides a function to write text to files.
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF8) and return the number of characters written.

    Creates the file if it doesn't exist, overwrites if it does exist.

    Args:
        filename (str): The name of the file to write to
        text (str): The text to write to the file

    Returns:
        int: The number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
