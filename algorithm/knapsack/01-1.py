# -*- coding:utf-8 -*-

"""
01 背包问题，物品不可分割，递归解法
@author: 付登龙
@file: 01-1.py
@time: 2019/02/25 7:48 PM
"""
from typing import List


class Knapsack(object):

    def __init__(self, num, weight, items: List[int]):
        self.num = num
        self.weight = weight
        self.items = items
        self.max_weight = float('-inf')
        self.records = {}

    def find(self, i, w):
        if i == self.num or self.weight == w:
            if w > self.max_weight:
                self.max_weight = w
            return
        if (i, w) in self.records: return
        self.records[(i, w)] = True
        self.find(i + 1, w)
        if w + self.items[i] <= self.weight:
            self.find(i + 1, w + self.items[i])


if __name__ == '__main__':

    knapsack = Knapsack(5, 9, [2, 2, 4, 5, 3])
    knapsack.find(0, 0)
    print(knapsack.max_weight)


