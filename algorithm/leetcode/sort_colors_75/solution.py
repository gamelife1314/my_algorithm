
class Solution:

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        buckets = [0] * 3

        # counts
        for num in nums:
            buckets[num] += 1

        # add
        for j in range(1, 3):
            buckets[j] = buckets[j] + buckets[j - 1]

        # sort
        tmp = [0] * len(nums)
        for num in nums:
            index = buckets[num] - 1
            tmp[index] = num
            buckets[num] -= 1

        nums[:] = tmp[:]


if __name__ == '__main__':
    s = Solution()
    colors = [1, 2, 0]
    s.sortColors(colors)
    print(colors)
