
class Solution:

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        counts = {}
        for num in nums:
            counts[num] = counts.setdefault(num, 0) + 1
        nums = sorted(counts.items(), key=lambda i: i[1], reverse=True)
        return [nums[i][0] for i in range(k)]

