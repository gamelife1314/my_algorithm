
class Solution:

    def permute(self, nums):
        
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if not nums: return [[]]

        results = []

        for i, n in enumerate(nums):
            for p in self.permute(nums[:i] + nums[i+1:]):
                results.append([n] + p)

        return results


if __name__ == "__main__":
    s = Solution()
    print(s.permute([1, 2]))
