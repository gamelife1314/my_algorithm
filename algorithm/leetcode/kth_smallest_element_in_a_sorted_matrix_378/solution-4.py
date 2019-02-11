import bisect


class Solution(object):

    def kthSmallest(self, matrix, k):
        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo < hi:
            mid = (lo + hi) // 2
            if sum(bisect.bisect_right(row, mid) for row in matrix) < k:
                lo = mid + 1
            else:
                hi = mid
        return lo


if __name__ == '__main__':
    m = [
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15]
    ]
    s = Solution()
    print(s.kthSmallest(m, 3))
