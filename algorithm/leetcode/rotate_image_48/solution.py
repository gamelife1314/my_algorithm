# -*- coding:utf-8 -*-

""" 
@author: 付登龙
@file: solution.py
@time: 2019/02/20 9:46 PM
"""

from typing import List


class Solution:

    def rotate(self, matrix: 'List[List[int]]') -> 'None':
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = list(zip(*matrix[::-1]))
