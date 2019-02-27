# -*- coding:utf-8 -*-

""" 
@author: 付登龙
@file: solution.py
@time: 2019/02/26 9:27 PM
"""


class Solution:
    cache = {1: 1, 0: 1}

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n not in self.cache:
            self.cache[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)

        return self.cache[n]
