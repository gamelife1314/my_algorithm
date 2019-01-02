# -*- coding:utf-8 -*-
from random import randint


def insert_sort(items: list) -> list:
    length = len(items)
    if length < 1:
        return items

    for i in range(1, length):
        value = items[i]
        j = i - 1
        while j >= 0:
            if items[j] > value:
                items[j+1] = items[j]
            else:
                break
            j -= 1
        items[j+1] = value
    return items


def test():
    for _ in range(40):
        items = [randint(1, 10 ** 5) for _ in range(50)]
        result1 = list(sorted(items))
        result2 = insert_sort(items)
        assert result2 == result1
