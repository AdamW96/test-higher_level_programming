#!/usr/bin/python3
def best_score(a_dictionary):
    """返回具有最大整数值的键"""
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)
