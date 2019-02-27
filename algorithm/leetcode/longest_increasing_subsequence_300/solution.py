# -*- coding:utf-8 -*-

""" 
@author: 付登龙
@file: solution.py
@time: 2019/02/27 9:43 PM
"""
from typing import List


class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        states = [0] * len(nums)
        states[0] = 1
        for i in range(1, len(nums)):
            states[i] = max([states[j] for j in range(i) if nums[j] < nums[i]] + [0]) + 1

        return max(states)


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18, 20]))
