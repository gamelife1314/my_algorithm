
class Solution:

    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        r, count, idx2, idx3, idx5 = [1] * n, 1, 0, 0, 0
        while count < n:
            min_ugly_number = min([r[idx2] * 2, r[idx3] * 3, r[idx5] * 5])
            if min_ugly_number == r[idx2] * 2:
                idx2 += 1
            if min_ugly_number == r[idx3] * 3:
                idx3 += 1
            if min_ugly_number == r[idx5] * 5:
                idx5 += 1
            r[count] = min_ugly_number
            count += 1
        return r[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.nthUglyNumber(1690))
