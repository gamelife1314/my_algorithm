# -*- coding:utf-8 -*-

"""
超时，让人很不爽
@author: 付登龙
@file: solution-1.py
@time: 2019/02/16 8:19 PM
"""
from typing import List


def merge_sort(nums: list):
    recursion(nums, 0, len(nums) - 1)


def recursion(nums, low, high):
    if low < high:
        mid = low + ((high - low) >> 1)
        recursion(nums, low, mid)
        recursion(nums, mid + 1, high)
        merge(nums, low, mid, high)


def merge(nums, low, mid, high):
    i, j = low, mid + 1
    tmp = []
    while i <= mid and j <= high:
        if nums[i] < nums[j]:
            tmp.append(nums[i])
            i += 1
        else:
            tmp.append(nums[j])
            j += 1
    rest_start = i if i <= mid else j
    rest_end = mid if i <= mid else high
    tmp.extend(nums[rest_start:rest_end + 1])
    nums[low: high + 1] = tmp


class Solution:

    def majorityElement(self, nums: 'List[int]') -> 'int':
        merge_sort(nums)
        print(nums)
        return nums[(len(nums) - 1) // 2]


if __name__ == '__main__':
    nums = [8, 9, 8, 9, 8]
    s = Solution()
    print(s.majorityElement(nums))
