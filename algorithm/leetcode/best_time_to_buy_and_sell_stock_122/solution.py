# -*- coding:utf-8 -*-

""" 
@author: 付登龙
@file: solution.py
@time: 2019/03/02 11:46 PM
"""


class Solution:

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        profit = 0
        for i in range(0, len(prices) - 1):
            if prices[i + 1] > prices[i]:
                profit += prices[i + 1] - prices[i]

        return profit


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))
