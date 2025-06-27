#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """按键的字母顺序打印字典"""
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))
