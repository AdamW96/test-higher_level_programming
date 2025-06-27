#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Replace an element of a list at a specific position.

    Args:
        my_list: The list to modify
        idx: The index where to replace the element
        element: The new element to place at the index

    Returns:
        The modified list, or original list if index is invalid
    """
    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
