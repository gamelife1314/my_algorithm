class Solution:

    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        length = len(citations)
        citations = list(sorted(citations))
        h_indexes = []
        for i in range(length - 1, -1, -1):
            h_indexes.append(min([length - i, citations[i]]))
        return 0 if not h_indexes else max(h_indexes)


if __name__ == '__main__':
    s = Solution()
    print(s.hIndex([25, 8, 5, 3, 3]))
