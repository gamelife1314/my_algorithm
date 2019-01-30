

class Solution:

    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i, num in enumerate(numbers):
            find = target - num
            low, high = i + 1, len(numbers) - 1
            while low <= high:
                mid = low + ((high - low) >> 1)
                if numbers[mid] == find:
                    return [i + 1, mid + 1]
                elif numbers[mid] > find:
                    high = mid - 1
                elif numbers[mid] < find:
                    low = mid + 1


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2, 2], 4))
