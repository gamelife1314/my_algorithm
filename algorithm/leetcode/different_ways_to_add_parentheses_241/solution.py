# -*- coding:utf-8 -*-

""" 
@author: 付登龙
@file: solution.py
@time: 2019/02/20 9:13 PM
"""
import operator
from typing import List


class Solution:

    def diffWaysToCompute(self, input: 'str') -> 'List[int]':

        if input.isdigit(): return [int(input)]

        operators = {
            '-': operator.sub,
            '+': operator.add,
            '*': operator.mul,
        }

        res = []
        for index, char in enumerate(input):
            if char in '+-*':
                prev = self.diffWaysToCompute(input[:index])
                next_ = self.diffWaysToCompute(input[index+1:])
                res.extend(map(lambda params: operators[char](*params), ((a, b) for a in prev for b in next_)))

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.diffWaysToCompute('2*3-4*5'))
