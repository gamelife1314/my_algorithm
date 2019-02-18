# -*- coding:utf-8 -*-

""" 
@author: 付登龙
@file: solution-1.py
@time: 2019/02/18 8:19 PM
"""
from typing import List


class UnionFind(object):

    def __init__(self, grid: List[List[str]]):
        row, col = len(grid), len(grid[0])
        self.roots = {(i * col + j): i * col + j for i in range(row) for j in range(col) if grid[i][j] == '1'}
        self.count = len(self.roots)
        print(self.count)

    def find(self, i):
        root = i
        while root != self.roots[root]:
            root = self.roots[root]
        while i != self.roots[i]:
            tmp = self.roots[i]
            self.roots[i] = root
            i = tmp
        return root

    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)
        if q_root != p_root:
            self.roots[q_root] = p_root
            self.count -= 1


class Solution:

    def numIslands(self, grid):

        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: return 0
        row, col = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        uf = UnionFind(grid)
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    for x, y in directions:
                        nr, nc = i + x, j + y
                        if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == '1':
                            uf.union(i * col + j, nr * col + nc)
        return uf.count


if __name__ == '__main__':
    s = Solution()
    print(s.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
