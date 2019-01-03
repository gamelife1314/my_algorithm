# -*- coding:utf-8 -*-

""" 
@author: 付登龙
@file: sqrt.py
@time: 2019/01/03 2:11 PM
"""

from random import randint
import math


def sqrt(num):
    low, high = 0, num if num > 1 or num == 0 else 1
    mid = high
    while abs(mid ** 2 - num) > 1e-6:
        if mid ** 2 - num > 0:
            high = mid
        else:
            low = mid
        mid = (low + high) / 2

    return float(mid)


def test():
    for _ in range(10 ** 4):
        num = randint(0, 2 ** 31)
        print(num)
        a = math.sqrt(num)
        b = sqrt(num)
        assert f"{a:.6f}" == f"{b:6f}"


if __name__ == '__main__':
    test()
    print(sqrt(2147395599))
