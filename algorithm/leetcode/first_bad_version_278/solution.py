
class Solution:

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left <= right:
            mid = left + ((right - left) >> 1)
            if isBadVersion(mid):
                if mid - 1 <= 0 or isBadVersion(mid - 1):
                    return mid
                right = mid - 1
            else:
                left = mid + 1
