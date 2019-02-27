# -*- coding:utf-8 -*-

""" 
@author: 付登龙
@file: solution-1.py
@time: 2019/02/27 10:09 PM
"""
import bisect
from typing import List


class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        lis = []
        for num in nums:
            pos = bisect.bisect_left(lis, num)
            if pos == len(lis):
                lis.append(num)
            else:
                lis[pos] = num
        return len(lis)


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18, 20]))
