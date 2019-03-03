# -*- coding:utf-8 -*-

""" 
@author: 付登龙
@file: solution.py
@time: 2019/03/02 11:38 PM
"""


class Solution:

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        profit = 0
        m = prices[0]

        for price in prices[1:]:
            if price - m > profit:
                profit = price - m
            if price < m:
                m = price

        return profit


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7, 1, 3, 5, 6, 4]))
