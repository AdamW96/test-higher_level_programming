#!/usr/bin/python3
"""
This module provides a function for text indentation.

The function adds new lines after specific punctuation marks.
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after each '.', '?', and ':'.

    Args:
        text (str): Text to be processed

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    i = 0
    while i < len(text):
        result += text[i]
        if text[i] in '.?:':
            result += '\n\n'
        i += 1

    # Split by lines and strip each line
    lines = result.split('\n')
    for i, line in enumerate(lines):
        if i == len(lines) - 1:
            print(line.strip(), end="")
        else:
            print(line.strip())
