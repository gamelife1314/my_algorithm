class Solution:

    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        container = set()
        return self.find(root, k, container)

    def find(self, root, k, container):
        if not root:
            return False
        if (k - root.val) in container:
            return True
        container.add(root.val)
        return self.find(root.left, k, container) or self.find(root.right, k, container)
