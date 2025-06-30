#!/usr/bin/python3
"""
This module provides a function to append text to files.
"""


def append_write(filename="", text=""):
    """
    Append a string at the end of a text file (UTF8) and return the number of characters added.

    Creates the file if it doesn't exist.

    Args:
        filename (str): The name of the file to append to
        text (str): The text to append to the file

    Returns:
        int: The number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
