#!/usr/bin/python3
"""
This module provides a function to read and print text files.
"""


def read_file(filename=""):
    """
    Read a text file (UTF8) and print it to stdout.

    Args:
        filename (str): The name of the file to read
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end='')
