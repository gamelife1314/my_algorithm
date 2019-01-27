# -*- coding:utf-8 -*-

""" 
@author: 付登龙
@file: solution-1.py
@time: 2019/01/26 9:44 PM
"""


class Solution:

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        nums = list(sorted(nums, reverse=True))
        return nums[k - 1]


