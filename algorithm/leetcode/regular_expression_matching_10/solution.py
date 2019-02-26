# -*- coding:utf-8 -*-

""" 
@author: 付登龙
@file: solution.py
@time: 2019/02/23 9:54 PM
"""


class Solution(object):

    def isMatch(self, text, pattern):
        if not pattern: return not text
        first_match = bool(text) and pattern[0] in {text[0], '.'}
        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])


if __name__ == '__main__':
    s = Solution()
    print(s.isMatch('', 'c*'))
