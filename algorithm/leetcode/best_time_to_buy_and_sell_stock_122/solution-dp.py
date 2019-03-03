# -*- coding:utf-8 -*-

""" 
@author: 付登龙
@file: solution-dp.py
@time: 2019/03/02 11:58 PM
"""


class Solution:

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if not prices: return 0

        days = len(prices)
        mp = [[0, 0] for _ in range(days)]
        mp[0] = [0, -prices[0]]
        for i in range(1, len(prices)):
            mp[i][0] = max(mp[i-1][0], mp[i-1][1] + prices[i])
            mp[i][1] = max(mp[i-1][1], mp[i-1][0] - prices[i])

        return max(mp[days - 1])


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))

