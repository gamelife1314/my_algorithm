import heapq


class Solution:

    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        return heapq.nsmallest(k, ([x, y] for x in nums1 for y in nums2), key=lambda item: item[0] + item[1])


if __name__ == '__main__':
    s = Solution()
    print(s.kSmallestPairs([1, 7, 11], [2, 4, 6], 3))
