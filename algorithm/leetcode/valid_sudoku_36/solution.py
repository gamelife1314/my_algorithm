from typing import List


class Solution:

    def isValidSudoku(self, board: 'List[List[str]]') -> 'bool':

        records = set()

        for row in range(9):
            for col in range(9):
                value = board[row][col]
                if value != '.':
                    if (row, value) in records or (value, col) in records or (row // 3, col // 3, value) in records:
                        return False
                    records.add((row, value))
                    records.add((value, col))
                    records.add((row // 3, col // 3, value))

        return True
