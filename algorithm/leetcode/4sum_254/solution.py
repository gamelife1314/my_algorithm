import collections


class Solution:

    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        AB = collections.Counter(a + b for a in A for b in B)
        return sum(AB[-c - d] for c in C for d in D)


if __name__ == '__main__':
    s = Solution()
    print(s.fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]))
