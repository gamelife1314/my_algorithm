from collections import Counter
import heapq


class Solution:

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = Counter(nums)
        print(counts, counts.keys())
        return heapq.nlargest(k, counts.keys(), key=counts.get)


if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequent([1, 1, 1, 2, 2, 3, 4, 5, 5, 5, 5], 2))
