#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """删除字典中的指定键"""
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
