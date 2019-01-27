# -*- coding:utf-8 -*-
from collections import deque


class Solution:

    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        window, out = deque(), []
        for index, num in enumerate(nums):
            if index >= k and window[0] <= index - k:
                window.popleft()
            while window and nums[window[-1]] <= num:
                window.pop()
            window.append(index)
            if index >= k - 1:
                out.append(nums[window[0]])
        return out


if __name__ == '__main__':
    s = Solution()
    print(s.maxSlidingWindow([1, 3, 1, 2, 0, 5], 3))
