# -*- coding:utf-8 -*-

"""
输入数据：
    物品价值：[3, 4, 2, 6]
    物品重量：[4, 2, 3, 1]
限制值：背包重量
期望值：物品价值
@author: 付登龙
@file: solution.py
@time: 2019/02/25 9:10 PM
"""
from typing import List


class Knapsack(object):

    def __init__(self, values: List[int], weights: List[int], limit: int):
        self.num = len(values)
        self.values = values
        self.weights = weights
        self.wl = limit  # weight limit

    def find(self):
        states = [[0 for _ in range(self.wl + 1)] for _ in range(self.num)]
        states[0][self.weights[0]] = self.values[0]
        for i in range(self.num):

            # 不放第 i 个物品
            for j in range(self.wl + 1):
                if states[i - 1][j] > 0:
                    states[i][j] = states[i - 1][j]

            # 放第 i 个物品
            for j in range(self.wl - self.weights[i] + 1):
                if states[i - 1][j] >= 0:
                    v = states[i - 1][j] + self.values[i]
                    if v > states[i][j + self.weights[i]]:
                        states[i][j + self.weights[i]] = v

        return max(states[self.num - 1])


if __name__ == '__main__':
    knapsack = Knapsack([3, 4, 8, 9, 6], [2, 2, 4, 6, 3], 9)
    print(knapsack.find())
