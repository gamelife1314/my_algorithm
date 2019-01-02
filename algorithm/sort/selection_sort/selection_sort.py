# -*- coding:utf-8 -*-
from random import randint


def selection_sort(items: list) -> list:
    length = len(items)
    if length < 1:
        return items
    for i in range(length - 1):
        min_index = i + 1
        for j in range(i + 2, length):
            if items[j] < items[min_index]:
                min_index = j
        if items[min_index] < items[i]:
            items[i], items[min_index] = items[min_index], items[i]
    return items


def test():
    for _ in range(20):
        items = [randint(1, 20) for _ in range(50)]
        result1 = list(sorted(items))
        result2 = selection_sort(items)
        assert result2 == result1

    for _ in range(20):
        items = [randint(1, 10 ** 6) for _ in range(50)]
        result1 = list(sorted(items))
        result2 = selection_sort(items)
        assert result2 == result1
