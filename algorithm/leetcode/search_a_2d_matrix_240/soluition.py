
class Solution:

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]: return False
        low, high = 0, len(matrix) - 1
        while low <= high:
            mid = low + ((high - low) >> 1)
            if matrix[mid][0] > target:
                high = mid - 1
            else:
                if mid == len(matrix) - 1 or matrix[mid+1][0] > target:
                    for i in range(mid, -1, -1):
                        if self.find(matrix[i], target):
                            return True
                    break
                else:
                    low = mid + 1
        return False

    def find(self, nums, target):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + ((high - low) >> 1)
            if nums[mid] == target:
                return True
            if nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False


if __name__ == '__main__':
    m = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    s = Solution()
    print(s.searchMatrix(m, 25))
    for items in m:
        for num in items:
            assert s.searchMatrix(m, num) is True
