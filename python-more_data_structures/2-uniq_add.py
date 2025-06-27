#!/usr/bin/python3
def uniq_add(my_list=[]):
    """将列表中所有唯一整数相加（每个整数只计算一次）"""
    return sum(set(my_list))
