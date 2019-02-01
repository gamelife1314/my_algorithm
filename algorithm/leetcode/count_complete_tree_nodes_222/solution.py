class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        self.num = 0
        self.prev_order(root)
        return self.num

    def prev_order(self, root):
        if not root: return
        self.num += 1
        self.prev_order(root.left)
        self.prev_order(root.right)
