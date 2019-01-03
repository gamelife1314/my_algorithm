# -*- coding:utf-8 -*-

"""
查找最后一个小于等于给定值的元素
@author: 付登龙
@file: bsearch_4.py
@time: 2019/01/03 3:35 PM
"""
from typing import List


def bsearch(items: List[int], value: int) -> int:
    low, high = 0, len(items) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if items[mid] > value:
            high = mid - 1
        else:
            if mid == len(items) - 1 or items[mid + 1] > value:
                return mid
            else:
                low = mid + 1
    return -1


if __name__ == '__main__':
    print(bsearch([1, 2, 2, 3, 4, 5], 2))
    print(bsearch([1, 2, 2, 3, 4, 5], 3))
