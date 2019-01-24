class Solution:

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """

        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + ((high - low) >> 1)
            if nums[mid] == target:
                return True

            while low < mid and nums[low] == nums[mid]:
                low += 1

            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            elif nums[low] > nums[mid]:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return False


if __name__ == '__main__':
    s = Solution()
    print(s.search([1, 1], 0))
    print(s.search([2, 5, 6, 0, 0, 1, 2], 3))
    print(s.search([2, 5, 6, 0, 0, 1, 2], 0))
    print(s.search([], 0))
    print(s.search([1, 3, 1, 1, 1], 3))


