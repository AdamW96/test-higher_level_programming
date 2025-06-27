#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replace an element in a list at a specific position without modifying the original list.

    Args:
        my_list: The original list
        idx: The index where to replace the element
        element: The new element to place at the index

    Returns:
        A new list with the element replaced, or a copy of the original list if index is invalid
    """
    if idx < 0:
        return my_list.copy()
    if idx >= len(my_list):
        return my_list.copy()
    new_list = my_list.copy()
    new_list[idx] = element
    return new_list
