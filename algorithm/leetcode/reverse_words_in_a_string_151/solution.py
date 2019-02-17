# -*- coding:utf-8 -*-

""" 
@author: 付登龙
@file: solution.py
@time: 2019/02/17 4:13 PM
"""


class Solution(object):

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return (" ".join(reversed(list(filter(lambda i: i != ' ', s.split(' ')))))).strip(' ')


if __name__ == '__main__':
    s = Solution()
    print(s.reverseWords(" a b"))
