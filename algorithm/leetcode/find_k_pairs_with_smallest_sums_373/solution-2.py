import heapq
import itertools


class Solution:

    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """

        streams = map(lambda u: ([u + v, u, v] for v in nums2), nums1)
        streams = heapq.merge(*streams)
        return [res[1:] for res in itertools.islice(streams, k)]


if __name__ == '__main__':
    s = Solution()
    print(s.kSmallestPairs([1, 7, 11], [2, 4, 6], 3))
