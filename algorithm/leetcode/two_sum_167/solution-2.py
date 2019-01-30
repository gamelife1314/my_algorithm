
class Solution:

    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        low, high = 0, len(numbers) - 1
        while low <= high:
            s = numbers[low] + numbers[high]
            if s == target:
                return [low + 1, high + 1]
            elif s > target:
                high -= 1
            else:
                low += 1


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))
