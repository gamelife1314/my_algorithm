# -*- coding:utf-8 -*-

""" 
@author: 付登龙
@file: bsearch.py
@time: 2019/01/03 1:53 PM
"""
from random import randint, choice


def bsearch(items: list, value):

    low, high = 0, len(items)
    while low <= high:
        mid = low + ((high - low) >> 1)
        if items[mid] == value:
            return mid
        elif items[mid] < value:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def test():
    for _ in range(40):
        items = [randint(1, 10 ** 8) for _ in range(randint(1, 40))]
        items.sort()
        find = choice(items)
        assert items.index(find) == bsearch(items, find)
