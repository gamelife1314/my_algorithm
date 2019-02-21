from typing import List


class Solution:

    def solveNQueens(self, n: 'int') -> 'List[List[str]]':
        solutions = []

        def recursion(row, result: list):
            if row == n:
                solutions.append(result)
                return
            for col in range(n):
                if isOk(row, col, result):
                    recursion(row + 1, result + [col])

        def isOk(row, col, result: list):
            left_up, right_up = col - 1, col + 1
            for i in range(row - 1, -1, -1):
                if result[i] == col or result[i] == left_up or result[i] == right_up:
                    return False
                left_up -= 1
                right_up += 1
            return True

        recursion(0, [])
        return [['.' * pos + 'Q' + '.' * (n - pos - 1) for pos in solution] for solution in solutions]


if __name__ == '__main__':
    s = Solution()
    print(s.solveNQueens(4))
