class TreeNode:

    def __init__(self):
        self.val = None
        self.left = None
        self.right = None


class Solution:

    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        numbers = []
        self.inOrder(root, numbers)
        low, high = 0, len(numbers) - 1
        while low < high:
            s = numbers[low] + numbers[high]
            if s == k:
                return True
            elif s > k:
                high -= 1
            else:
                low += 1
        return False

    def inOrder(self, root, nums):
        if not root:
            return
        self.inOrder(root.left, nums)
        nums.append(root.val)
        self.inOrder(root.right, nums)

