
class Solution:

    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            if count[num] == 2:
                return num
