#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """Print all integers of a list, one per line.

    Args:
        my_list: List of integers to print
    """
    for integer in my_list:
        print("{:d}".format(integer))
