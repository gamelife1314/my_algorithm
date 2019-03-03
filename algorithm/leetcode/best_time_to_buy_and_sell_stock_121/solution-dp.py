# -*- coding:utf-8 -*-

"""
[
    [
        [0, 1],
        [0, 1],
    ]
]
@author: 付登龙
@file: solution-dp.py
@time: 2019/03/03 12:09 AM
"""


class Solution(object):

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if not prices: return 0

        profit = [[[0, 0] for _ in range(2)] for _ in range(len(prices))]
        profit[0][0][0], profit[0][0][1] = 0, -prices[0]
        profit[0][1][0], profit[0][1][1] = float('-inf'), float('-inf')

        for day in range(1, len(prices)):
            profit[day][0][0] = profit[day-1][0][0]
            profit[day][0][1] = max(profit[day-1][0][1], profit[day-1][0][0] - prices[day])

            profit[day][1][0] = max(profit[day-1][1][0], profit[day-1][0][1] + prices[day])
            profit[day][1][1] = max(profit[day-1][1][1], profit[day-1][1][0] - prices[day])

        end = len(prices) - 1
        return max(profit[end][0][0], profit[end][1][0])


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7, 6, 5, 4, 3]))
