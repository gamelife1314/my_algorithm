# -*- coding:utf-8 -*-

""" 
@author: 付登龙
@file: solution.py
@time: 2019/02/17 8:35 PM
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: 'TreeNode', s: 'int') -> 'bool':
        if not root: return False
        if root.val == s and root.left is None and root.right is None: return True
        return self.hasPathSum(root.left, s - root.val) or self.hasPathSum(root.right, s - root.val)
