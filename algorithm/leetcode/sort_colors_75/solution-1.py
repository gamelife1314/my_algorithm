
class Solution:

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        zero, second = 0, length - 1
        for i in range(length):
            while i < second and nums[i] == 2:
                nums[i], nums[second] = nums[second], nums[i]
                second -= 1
            while i > zero and nums[i] == 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1


if __name__ == '__main__':
    s = Solution()
    colors = [1, 2, 0]
    s.sortColors(colors)
    print(colors)
