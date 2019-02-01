class Solution:

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if not matrix or not matrix[0]: return False

        line, low, high = 0, 0, len(matrix) - 1
        while low <= high:
            mid = low + ((high - low) >> 1)
            if matrix[mid][0] > target:
                high = mid - 1
            else:
                if mid == len(matrix) - 1 or matrix[mid+1][0] > target:
                    line = mid
                    break
                else:
                    low = mid + 1

        low, high = 0, len(matrix[line]) - 1
        while low < high:
            mid = low + ((high - low) >> 1)
            if matrix[line][mid] == target:
                return True
            elif matrix[line][mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return True if matrix[line][low] == target else False


if __name__ == '__main__':
    s = Solution()
    m = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    for i in range(len(m)):
        for j in range(len(m[0])):
            assert s.searchMatrix(m, m[i][j]) is True
    m = [
        [0, 1, 2, 3]
    ]
    print(s.searchMatrix(m, 1))
