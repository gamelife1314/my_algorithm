from collections import Counter


class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = Counter(nums)
        return counter.most_common(1)[0][0]


if __name__ == '__main__':
    s = Solution()
    print(s.findDuplicate([1, 3, 4, 2, 2]))

