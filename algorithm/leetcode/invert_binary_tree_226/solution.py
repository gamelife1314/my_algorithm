# -*- coding:utf-8 -*-

""" 
@author: 付登龙
@file: solution.py
@time: 2019/02/17 8:16 PM
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        if not root or (root.left is None and root.right is None): return

        self.invertTree(root.left)
        self.invertTree(root.right)

        root.left, root.right = root.right, root.left
