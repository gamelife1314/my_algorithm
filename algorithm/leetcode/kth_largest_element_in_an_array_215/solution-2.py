# -*- coding:utf-8 -*-

""" 
@author: 付登龙
@file: solution-2.py
@time: 2019/01/26 10:00 PM
"""


def partition(nums: list, low, high):
    pivot = nums[high]
    i = low
    for j in range(low, high):
        if nums[j] >= pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[high] = nums[high], nums[i]
    return i


def select(nums: list, k):
    i = partition(nums, 0, len(nums) - 1)
    if i + 1 == k:
        return nums[i]
    if i + 1 > k:
        return select(nums[0:i], k)
    if i + 1 < k:
        return select(nums[i+1:], k - i - 1)


class Solution:

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return select(nums, k)


if __name__ == '__main__':
    print(select([3], 1))

