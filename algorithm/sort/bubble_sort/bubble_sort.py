# -*- coding:utf-8 -*-
from random import randint


def bubble_sort(items: list) -> list:
    length = len(items)
    if length < 1:
        return items

    for i in range(length):
        exchange = False
        for j in range(length - i - 1):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
                if not exchange:
                    exchange = True
        if not exchange:
            break
    return items


def test():

    for _ in range(20):
        items = [randint(1, 20) for _ in range(50)]
        result1 = list(sorted(items))
        result2 = bubble_sort(items)
        assert result2 == result1

    for _ in range(20):
        items = [randint(1, 10 ** 5) for _ in range(50)]
        result1 = list(sorted(items))
        result2 = bubble_sort(items)
        assert result2 == result1

