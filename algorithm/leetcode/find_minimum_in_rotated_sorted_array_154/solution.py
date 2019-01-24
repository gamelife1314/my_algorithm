class Solution:

    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + ((right - left) >> 1)
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1
        return nums[left]


if __name__ == '__main__':
    s = Solution()
    assert s.findMin([2, 2, 2, 0, 2]) == 0
    assert s.findMin([2]) == 2
    assert s.findMin([4, 0, 1, 2, 3]) == 0
    assert s.findMin([3, 4, 5, 1, 2]) == 1
    assert s.findMin([2, 2, 2, 2]) == 2
    assert s.findMin([4, 4, 1, 2, 3]) == 1
    assert s.findMin([4, 4, 1, 2]) == 1
    assert s.findMin([4, 4, 1, 3, 3]) == 1
    assert s.findMin([4, 4, 1, 3]) == 1
    assert s.findMin([3, 1, 3]) == 1
