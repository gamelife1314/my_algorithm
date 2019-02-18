# -*- coding:utf-8 -*-

""" 
@author: 付登龙
@file: solution.py
@time: 2019/02/18 7:54 PM
"""


class Solution:

    count = 0

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def numIslands(self, grid):

        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: return 0
        row, col = len(grid), len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    self.count += 1
                    self.dfs(grid, row, col, i, j)
        return self.count

    def dfs(self, grid, row, col, i, j):
        grid[i][j] = '0'
        for x, y in self.directions:
            if 0 <= (i + x) < row and 0 <= (j + y) < col and grid[i + x][j + y] == '1':
                self.dfs(grid, row, col, i + x, j + y)


if __name__ == '__main__':
    s = Solution()
    print(s.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))