from collections import UserString


class LargerNumKey(UserString):

    def __lt__(self, y):
        return self + y > y + self


class Solution:

    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))

        return '0' if len(largest_num) > 0 and largest_num[0] == '0' else largest_num


if __name__ == '__main__':
    s = Solution()
    print(s.largestNumber([]))
