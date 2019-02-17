# -*- coding:utf-8 -*-

""" 
@author: 付登龙
@file: solution-2.py
@time: 2019/02/16 7:57 PM
"""


class Solution:

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        results = []
        self.find_n_sum(nums, 0, 3, [], results)
        return results

    def find_n_sum(self, nums, target, n, result, results):
        if len(nums) < n or n < 2: return

        if n == 2:
            low, high = 0, len(nums) - 1
            while low < high:
                if nums[low] + nums[high] == target:
                    results.append(result + [nums[low], nums[high]])
                    low += 1
                    high -= 1
                    while low < high and nums[low] == nums[low - 1]:
                        low += 1
                    while high > low and nums[high] == nums[high + 1]:
                        high -= 1
                elif nums[low] + nums[high] < target:
                    low += 1
                else:
                    high -= 1
        else:
            if target <= nums[-1] * n:
                for i in range(len(nums) - n + 1):
                    if target < nums[i] * n:
                        break
                    if i == 0 or nums[i - 1] != nums[i]:
                        self.find_n_sum(nums[i+1:], target - nums[i], n - 1, result + [nums[i]], results)


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([0, 0, 0, 0]))
