# -*- coding:utf-8 -*-

"""
超时
@author: 付登龙
@file: solution.py
@time: 2019/02/27 8:56 PM
"""


class Solution:

    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle or not triangle[0]: return 0

        results = []
        length = len(triangle)

        def dfs(i, j, s):
            if i >= length:
                results.append(s)
                return

            s += triangle[i][j]
            dfs(i + 1, j, s)
            dfs(i + 1, j + 1, s)

        dfs(0, 0, 0)

        return min(results)


if __name__ == '__main__':
    triangle = [
        [2],
        [3, 2],
        [6, 5, 4],
        [1, 1, 10, 100],
    ]
    s = Solution()
    print(s.minimumTotal(triangle))


