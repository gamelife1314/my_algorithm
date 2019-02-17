# -*- coding:utf-8 -*-

""" 
@author: 付登龙
@file: solution.py
@time: 2019/02/16 8:14 PM
"""
from typing import List


class Solution:

    def majorityElement(self, nums: 'List[int]') -> 'int':
        nums.sort()
        return nums[len(nums) - 1 // 2]
