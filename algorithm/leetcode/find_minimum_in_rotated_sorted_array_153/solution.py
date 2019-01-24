class Solution:

    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + ((high - low) >> 1)
            if nums[mid] <= nums[mid - 1]:
                return nums[mid]
            else:
                if nums[mid] > nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1


if __name__ == '__main__':
    s = Solution()
    print(s.findMin([4, 0, 1, 2, 3]))
    print(s.findMin([3, 4, 5, 1, 2]))
    print(s.findMin([3]))
