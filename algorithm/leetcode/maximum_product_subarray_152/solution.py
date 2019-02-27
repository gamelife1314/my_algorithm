# -*- coding:utf-8 -*-

""" 
@author: 付登龙
@file: solution.py
@time: 2019/02/27 10:26 PM
"""


class Solution:

    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        r = [[nums[0], nums[0]]]
        for i in range(1, len(nums)):
            r.append([
                max(nums[i] * r[i-1][0], nums[i] * r[i-1][1], nums[i]),
                min(nums[i] * r[i-1][0], nums[i] * r[i-1][1], nums[i]),
            ])
        return max([a[0] for a in r])


if __name__ == '__main__':
    s = Solution()
    print(s.maxProduct([98, 3, -2, 4]))
