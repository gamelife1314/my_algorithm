# -*- coding:utf-8 -*-

""" 
@author: 付登龙
@file: counting_sort.py
@time: 2019/01/03 10:49 AM
"""
from random import randint
from typing import List


def counting_sort(items: List[int]) -> List[int]:
    length = len(items)
    max_item = max(items)
    bucket = [0] * (max_item + 1)

    # 计数
    for item in items:
        bucket[item] += 1

    # 累加
    for i in range(1, max_item + 1):
        bucket[i] = bucket[i - 1] + bucket[i]

    # 排序
    tmp = [0] * length
    for i in range(length - 1, -1, -1):
        index = bucket[items[i]] - 1
        tmp[index] = items[i]
        bucket[items[i]] -= 1

    return tmp


def test():
    for _ in range(40):
        items = [randint(1, 10) for _ in range(randint(1, 30))]
        result1 = list(sorted(items))
        result2 = counting_sort(items)
        assert result2 == result1


if __name__ == '__main__':
    test()
