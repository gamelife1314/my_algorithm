from functools import reduce


class Solution:

    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """

        result = reduce(self.merge, matrix, [])
        return result[k - 1]

    def merge(self, prev, line):
        if not prev: return line
        if not line: return prev

        i, j, index, prev_len, line_len = 0, 0, 0, len(prev), len(line)
        result = [None] * (prev_len + line_len)
        while i < prev_len and j < line_len:
            if prev[i] <= line[j]:
                result[index] = prev[i]
                i += 1
            else:
                result[index] = line[j]
                j += 1
            index += 1

        if i < prev_len: result[index:] = prev[i:]
        if j < line_len: result[index:] = line[j:]

        return result


if __name__ == '__main__':
    s = Solution()
    m = [
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15]
    ]
    print(s.kthSmallest(m, 7))
