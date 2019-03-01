# -*- coding:utf-8 -*-

""" 
@author: 付登龙
@file: solution.py
@time: 2019/02/25 8:09 PM
"""
from typing import List


class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        max_ = amount + 1
        states = [max_] * (amount + 1)
        states[0] = 0
        for i in range(1, amount + 1):
            states[i] = min([states[i - coin] + 1 for coin in coins if coin <= i] + [states[i]])
        return states[amount] if states[amount] <= amount else -1


if __name__ == '__main__':
    s = Solution()
    print(s.coinChange([1], 11))
