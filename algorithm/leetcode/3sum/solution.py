

class Solution:

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = set()
        for index, value in enumerate(nums[:-2]):
            d = {}
            for x in nums[index + 1:]:
                if x not in d:
                    d[-value-x] = True
                else:
                    result.add((value, -value-x, x))
        return list(map(list, result))


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))
