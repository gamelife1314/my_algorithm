# -*- coding:utf-8 -*-

""" 
@author: 付登龙
@file: quick_sort.py
@time: 2019/01/02 9:19 PM
"""

from typing import List
from random import randint


def quick_sort(items: List[int]) -> List[int]:
    recursion(items, 0, len(items) - 1)
    return items


def recursion(items: List[int], low: int, high: int):
    if low < high:
        point = partition(items, low, high)
        recursion(items, low, point - 1)
        recursion(items, point + 1, high)


def partition(items: List[int], low: int, high: int):
    pivot = items[high]
    i = low
    for j in range(low, high):
        if items[j] < pivot:
            items[i], items[j] = items[j], items[i]
            i += 1
    items[i], items[high] = items[high], items[i]
    return i


def test():
    for _ in range(40):
        items = [randint(1, 10 ** 6) for _ in range(50)]
        result1 = list(sorted(items))
        result2 = quick_sort(items)
        assert result2 == result1
