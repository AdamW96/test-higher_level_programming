#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """在新列表中替换所有指定元素"""
    return [replace if x == search else x for x in my_list]
