# -*- coding:utf-8 -*-

""" 
@author: 付登龙
@file: solution.py
@time: 2019/02/17 4:04 PM
"""
from typing import List


class Solution:

    def reverseString(self, s: 'List[str]') -> 'None':
        """
        Do not return anything, modify s in-place instead.
        """
        length = len(s)
        for i in range(length // 2):
            s[i], s[length - i - 1] = s[length - i - 1], s[i]


if __name__ == '__main__':
    chars = ["h", "e", "l", "o"]
    s = Solution()
    s.reverseString(chars)
    print(chars)
