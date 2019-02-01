
class Solution:

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        first = self.find(nums, target)
        if first == -1: return [-1, -1]
        return [first, self.find(nums, target, first, False)]

    def find(self, nums, target, low=0, first=True):

        low, high = low, len(nums) - 1
        while low <= high:
            mid = low + ((high - low) >> 1)
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                if first:
                    if mid == 0 or nums[mid - 1] != target:
                        return mid
                    else:
                        high = mid - 1
                else:
                    if mid == len(nums) - 1 or nums[mid + 1] != target:
                        return mid
                    else:
                        low = mid + 1
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.searchRange([], 10))
