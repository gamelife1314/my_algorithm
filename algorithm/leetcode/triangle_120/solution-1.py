# -*- coding:utf-8 -*-

""" 
@author: 付登龙
@file: solution-1.py
@time: 2019/02/27 9:08 PM
"""


class Solution:

    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        if not triangle or not triangle[0]: return 0

        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] = min(triangle[i+1][j], triangle[i+1][j+1]) + triangle[i][j]

        return triangle[0][0]


if __name__ == '__main__':
    triangle = [
        [2],
        [3, 2],
        [6, 5, 4],
        [1, 1, 10, 100],
    ]
    s = Solution()
    print(s.minimumTotal(triangle))