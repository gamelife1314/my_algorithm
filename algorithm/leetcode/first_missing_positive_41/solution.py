# -*- coding:utf-8 -*-

""" 
@author: 付登龙
@file: solution.py
@time: 2019/02/16 10:49 PM
"""
from typing import List


class Solution:

    def firstMissingPositive(self, nums: 'List[int]') -> 'int':

        i, length = 0, len(nums)
        while i < length:
            print(nums)
            if nums[i] != i + 1 and 1 <= nums[i] <= length and nums[nums[i] - 1] != nums[i]:
                index = nums[i] - 1
                nums[i], nums[index] = nums[index], nums[i]
            else:
                i += 1

        for i in range(length):
            if nums[i] != i + 1:
                return i + 1

        return length + 1


if __name__ == '__main__':
    s = Solution()
    print(s.firstMissingPositive([7, 8, 9, 11, 12]))
