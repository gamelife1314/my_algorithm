from typing import List


class Solution:

    def solveNQueens(self, n: 'int') -> 'List[List[str]]':

        solutions = []


        def dfs(queens, xy_sum, xy_diff):
            row = len(queens)
            if row == n:
                solutions.append(queens)
                return
            
            for col in range(n):
                if col not in queens and row + col not in xy_sum and row - col not in xy_diff:
                    dfs(queens + [col], [row + col] + xy_sum, [row - col] + xy_diff)

        dfs([], [], [])

        return [['.' * pos + 'Q' + '.' * (n - pos - 1) for pos in solution] for solution in solutions]


if __name__ == "__main__":
    s = Solution()
    print(s.solveNQueens(4))


