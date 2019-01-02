# -*- coding:utf-8 -*-
from typing import List
from random import randint


def merge_sort(items: List[int]) -> List[int]:
    recursion(items, 0, len(items) - 1)
    return items


def recursion(items: List[int], low: int, high: int):
    if low < high:
        mid = low + (high - low) // 2
        recursion(items, low, mid)
        recursion(items, mid + 1, high)
        merge(items, low, mid, high)


def merge(items: List[int], low: int, mid: int, high: int):
    i, j = low, mid + 1
    tmp = []
    while i <= mid and j <= high:
        if items[i] < items[j]:
            tmp.append(items[i])
            i += 1
        else:
            tmp.append(items[j])
            j += 1
    rest_start = i if i <= mid else j
    rest_end = mid if i <= mid else high
    tmp.extend(items[rest_start:rest_end + 1])
    items[low:high+1] = tmp


def test():
    for _ in range(40):
        items = [randint(1, 10 ** 5) for _ in range(50)]
        result1 = list(sorted(items))
        result2 = merge_sort(items)
        assert result2 == result1
