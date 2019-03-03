# -*- coding:utf-8 -*-

""" 
@author: 付登龙
@file: solution.py
@time: 2019/03/03 10:11 PM
"""


class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        s_len, p_len = len(s), len(p)
        if len(p) - p.count('*') > s_len:
            return False
        dp = [[False for _ in range(s_len + 1)] for _ in range(p_len + 1)]
        dp[0][0] = True
        for i in range(1, p_len + 1):
            dp[i][0] = dp[i-1][0] and (p[i-1] == '*')
            for j in range(1, s_len + 1):
                if p[i-1] != '*':
                    dp[i][j] = dp[i-1][j-1] and (p[i-1] == '?' or p[i-1] == s[j-1])
                else:
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
        return dp[p_len][s_len]


if __name__ == '__main__':
    s = Solution()
    print(s.isMatch('aa', '?*'))

