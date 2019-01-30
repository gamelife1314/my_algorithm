
class Solution:

    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        check = {}
        for i, num in enumerate(numbers):
            if num in check:
                return [check[num] + 1, i + 1]
            check[target - num] = i