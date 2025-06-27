#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Find all multiples of 2 in a list.

    Args:
        my_list: List of integers to check

    Returns:
        A new list with True or False values indicating whether
        each corresponding element is divisible by 2
    """
    result_list = []
    for integer in my_list:
        result_list.append(integer % 2 == 0)
    return result_list
