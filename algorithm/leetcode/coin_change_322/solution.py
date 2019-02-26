# -*- coding:utf-8 -*-

""" 
@author: 付登龙
@file: solution.py
@time: 2019/02/25 8:09 PM
"""
from typing import List


class Solution:

    num = 0

    def coinChange(self, coins: List[int], amount: int) -> int:
        self.recursion(coins, amount)
        return self.num

    def recursion(self, coins: List[int], amount: int):
        print(coins, amount)
        if not coins:
            if amount > 0:
                self.num = -1
            return
        max_coin = max(coins)
        tmp = amount // max_coin
        self.num += tmp
        coins.remove(max_coin)
        self.recursion(coins, amount - tmp * max_coin)


if __name__ == '__main__':
    s = Solution()
    print(s.coinChange([186, 419, 83, 408], 6249))
