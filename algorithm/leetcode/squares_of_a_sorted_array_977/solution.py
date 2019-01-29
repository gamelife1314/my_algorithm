
class Solution:

    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        N = len(A)
        j = 0
        while j < N and A[j] < 0:
            j += 1
        i = j - 1
        result = []
        while 0 <= i and j < N:
            i_s, j_s = A[i] ** 2, A[j] ** 2
            if i_s < j_s:
                result.append(i_s)
                i -= 1
            else:
                result.append(j_s)
                j += 1
        while i >= 0:
            result.append(A[i] ** 2)
            i -= 1
        while j < N:
            result.append(A[j] ** 2)
            j += 1
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.sortedSquares([-3, -3, 1, 2]))
