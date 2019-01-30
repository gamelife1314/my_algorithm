
class Solution(object):

    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        low, high = 0, num
        mid = high

        while abs(mid ** 2 - num) > 1e-6:
            if mid ** 2 - num > 1e-6:
                high = mid
            else:
                low = mid
            mid = low + ((high - low) / 2)

        return True if abs(round(mid) - mid) < 1e-6 else False


if __name__ == '__main__':
    s = Solution()
    for num in [1, 3, 4, 14, 100]:
        print(s.isPerfectSquare(num))

