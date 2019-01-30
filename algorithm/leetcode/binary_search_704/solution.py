
class Solution:

    def search(self, nums, target):

        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + ((high - low) >> 1)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high -= 1
            else:
                low += 1

        return -1

