# -*- coding:utf-8 -*-

""" 
@author: 付登龙
@file: solution.py
@time: 2019/02/17 3:12 PM
"""
from collections import deque


class Solution:

    def longestValidParentheses(self, s: 'str') -> 'int':
        q = deque()
        n = 0
        q.append(-1)
        for index, char in enumerate(s):
            if char == '(':
                q.append(index)
            else:
                q.pop()
                if len(q) == 0:
                    q.append(index)
                else:
                    n = max(n, index - q[-1])
        return n


if __name__ == '__main__':
    s = Solution()
    print(s.longestValidParentheses('()()'))
