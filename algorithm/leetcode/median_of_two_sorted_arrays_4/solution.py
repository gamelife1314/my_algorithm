# -*- coding:utf-8 -*-

""" 
@author: 付登龙
@file: solution.py
@time: 2019/02/20 8:37 PM
"""
from typing import List


class Solution:

    def findMedianSortedArrays(self, nums1: 'List[int]', nums2: 'List[int]') -> 'float':
        tmp = self.merge(nums1, nums2)
        if not tmp:
            return .0
        else:
            l = len(tmp)
            if l & 1:
                return float(tmp[(l - 1) >> 1])
            else:
                return (tmp[l >> 1] + tmp[(l >> 1) - 1]) / 2.0

    def merge(self, nums1, nums2):
        i, j, m, n = 0, len(nums1), 0, len(nums2)
        tmp = []
        while i < j and m < n:
            if nums1[i] <= nums2[m]:
                tmp.append(nums1[i])
                i += 1
            else:
                tmp.append(nums2[m])
                m += 1
        if i < j:
            tmp.extend(nums1[i:j])
        if m < n:
            tmp.extend(nums2[m:n])
        return tmp


if __name__ == '__main__':
    s = Solution()
    print(s.findMedianSortedArrays([1, 2], [3, 4]))

