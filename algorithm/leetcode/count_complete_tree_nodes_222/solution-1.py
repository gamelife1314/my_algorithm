
class Solution:

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        if left_height > right_height:
            return 2 ** right_height + self.countNodes(root.left)
        else:
            return 2 ** left_height + self.countNodes(root.right)

    def height(self, root):
        h = 0
        while root:
            h += 1
            root = root.left
        return h
