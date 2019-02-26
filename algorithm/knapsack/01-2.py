# -*- coding:utf-8 -*-

"""
01 背包问题，动态规划解法
@author: 付登龙
@file: 01-2.py
@time: 2019/02/25 8:36 PM
"""
from typing import List


class Knapsack:

    def __init__(self, num, weight, items: List[int]):
        self.num = num
        self.weight = weight
        self.items = items

    def find(self):
        states = [[False for _ in range(self.weight + 1)] for _ in range(self.num)]
        states[0][0] = True
        states[0][self.items[0]] = True

        for i in range(1, self.num):
            # 不放第 i 个物品
            for j in range(self.weight + 1):
                if states[i - 1][j]: states[i][j] = True
            # 放第 i 个物品
            for j in range(self.weight - self.items[i] + 1):
                if states[i - 1][j]:
                    states[i][j + self.items[i]] = True

        for i in range(self.weight, -1, -1):
            if states[self.num - 1][i]: return i

        return 0

    def find2(self):
        states = [False] * (self.weight + 1)
        states[0] = True
        states[self.items[0]] = True
        for i in range(1, self.num):
            for w in range(self.weight - self.items[i] + 1):
                if states[w]:
                    states[w + self.items[i]] = True

        return states.index(True, -1)


if __name__ == '__main__':
    knapsack = Knapsack(5, 9, [2, 2, 4, 5, 3])
    print(knapsack.find())
    print(knapsack.find2())
