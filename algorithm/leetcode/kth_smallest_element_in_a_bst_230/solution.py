
class Solution:

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        nums = []
        self.in_order(root, nums, k)
        return nums[-1] if len(nums) == k else None

    def in_order(self, root, nums, k):
        if not root or len(nums) == k:
            return
        self.in_order(root.left, nums, k)
        if len(nums) < k:
            nums.append(root.val)
        self.in_order(root.right, nums, k)
