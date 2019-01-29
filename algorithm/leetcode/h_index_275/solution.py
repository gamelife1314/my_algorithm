class Solution:

    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        left, right, length = 0, len(citations) - 1, len(citations)
        while left <= right:
            mid = left + ((right - left) >> 1)
            if citations[mid] == length - mid:
                return length - mid
            elif citations[mid] > length - mid:
                right = mid - 1
            else:
                left = mid + 1
        return length - left


if __name__ == '__main__':
    s = Solution()
    print(s.hIndex([0]))
