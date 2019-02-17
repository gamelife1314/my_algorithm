# -*- coding:utf-8 -*-

""" 
@author: 付登龙
@file: solution.py
@time: 2019/02/17 3:54 PM
"""


class Solution:

    def mySqrt(self, num):
        """
        :type x: int
        :rtype: int
        """

        low, high = 0, 1 if 0 < num <= 1 else num
        mid = high

        while abs(mid ** 2 - num) > 1e-6:
            if mid ** 2 - num > 0:
                high = mid
            else:
                low = mid

            mid = (low + high) / 2

        return int(mid)


if __name__ == '__main__':
    s = Solution()
    print(s.mySqrt(100))
