#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """返回所有值乘以2的新字典"""
    return {key: value * 2 for key, value in a_dictionary.items()}
