# -*- coding:utf-8 -*-

"""
统计列表的逆序度
@author: 付登龙
@file: count_inverted_sequence.py
@time: 2019/02/18 9:46 PM
"""


class Counter:

    def __init__(self, nums: list):
        self.num = 0
        self.nums = nums

    def count(self):
        self.recursion(self.nums, 0, len(self.nums) - 1)
        return self.num

    def recursion(self, nums, low, high):
        if low < high:
            mid = low + ((high - low) >> 1)
            self.recursion(nums, low, mid)
            self.recursion(nums, mid + 1, high)
            self.merge(nums, low, mid, high)

    def merge(self, nums, low, mid, high):
        i, j = low, mid + 1
        tmp = []

        while i <= mid and j <= high:
            if nums[i] <= nums[j]:
                tmp.append(nums[i])
                i += 1
            else:
                tmp.append(nums[j])
                j += 1
                self.num += (mid - i + 1)

        m = i if i <= mid else j
        n = mid if i <= mid else high
        tmp.extend(nums[m:n+1])
        nums[low:high+1] = tmp


if __name__ == '__main__':
    counter = Counter([2, 4, 3, 1, 5, 6])
    print(counter.count())
