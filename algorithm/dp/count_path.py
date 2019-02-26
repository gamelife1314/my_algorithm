# -*- coding:utf-8 -*-

""" 
@author: 付登龙
@file: count_path.py
@time: 2019/02/26 8:14 PM
"""
from typing import List, Tuple


class CountPath(object):

    def __init__(self, grid: List[List[int]], start: Tuple[int, int], end: Tuple[int, int]) -> None:
        self.grid = grid
        self.start = start
        self.end = end
        self.row = len(grid)
        self.col = len(grid[0])

    def count(self, row, col):
        if self.is_stone(row, col): return 0
        if self.is_at_end(row, col): return 1
        return self.count(row + 1, col) + self.count(row, col + 1)

    def is_stone(self, row, col):
        return row >= self.row or col >= self.col or self.grid[row][col] == 1

    def is_at_end(self, row, col):
        return (row, col) == self.end

    def dp(self):
        states = [[0 for _ in range(self.col)] for _ in range(self.row)]
        end = (self.row - 1, self.col - 1)
        for row in range(self.row - 1, -1, -1):
            for col in range(self.col - 1, -1, -1):

                if self.grid[row][col] == 1 or (row, col) == end:
                    states[row][col] = 0
                    continue

                if (row + 1, col) == end or (row, col + 1) == end:
                    states[row][col] = 1
                    continue

                if row + 1 >= self.row:
                    states[row][col] = states[row][col + 1]
                    continue

                if col + 1 >= self.col:
                    states[row][col] = states[row + 1][col]
                    continue

                states[row][col] = states[row][col + 1] + states[row + 1][col]

        return states[0][0]


if __name__ == '__main__':
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [1, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 1, 0],
        [0, 1, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ]
    count_path = CountPath(grid, (0, 0), (7, 7))
    print(count_path.count(0, 0))
    print(count_path.dp())

