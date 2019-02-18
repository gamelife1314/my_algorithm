# -*- coding:utf-8 -*-

"""
并差集，用于判定是否是同一个朋友圈，采用路径压缩，在查找的时候压缩
@author: 付登龙
@file: union_find.py
@time: 2019/02/18 7:33 PM
"""
from typing import List


class UnionFind(object):

    def __init__(self, grid: List[List[str]]):
        """
        :param grid: 二位矩阵，字符 '0' 或者 '1'
        """
        row, col = len(grid), len(grid[0])
        self.roots = {(i * col + j): (i * col + j) for i in range(row) for j in range(col) if grid[i][j] == '1'}
        self.count = len(self.roots)

    def find(self, i):
        root = i
        while root != self.roots[root]:
            root = self.roots[root]
        while i != self.roots[i]:
            tmp = self.roots[i]
            self.roots[i] = root
            i = tmp

    def union(self, p, q):
        p_root, q_root = self.find(p), self.find(q)
        if p_root != q_root:
            self.roots[p_root] = q_root
            self.count -= 1

