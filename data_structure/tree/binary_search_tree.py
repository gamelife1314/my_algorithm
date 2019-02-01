# -*- coding:utf-8 -*-

"""
二叉搜索树
@author: 付登龙
@file: binary_search_tree.py
@time: 2019/01/13 10:12 AM
"""
from random import randint, choice
from typing import Optional, List


class TreeNode(object):

    def __init__(self, key: Optional[int]=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


class BinarySearchTree(object):

    def __init__(self, root: Optional[TreeNode] = None):
        self.root = root

    def find(self, key: int) -> Optional[TreeNode]:
        node = self.root
        while node:
            if key > node.key:
                node = node.right
            elif key < node.key:
                node = node.left
            else:
                return node
        return None

    def insert(self, key: int):
        if self.root is None:
            self.root = TreeNode(key)
            return

        node = self.root
        while node is not None:
            if key > node.key:
                if node.right is None:
                    node.right = TreeNode(key)
                    return
                node = node.right
            elif key < node.key:
                if node.left is None:
                    node.left = TreeNode(key)
                    return
                node = node.left
            else:
                return

    def delete(self, key: int):
        node, node_parent = self.root, None

        while node is not None and node.key != key:
            node_parent = node
            if key > node.key:
                node = node.right
            else:
                node = node.left

        if node is None:
            return

        # 要删除的节点有左右子树
        if node.left is not None and node.right is not None:  # 查找右子树最小节点
            right_min_node = node.right
            right_min_node_parent = node
            while right_min_node.left is not None:
                right_min_node_parent = right_min_node
                right_min_node = right_min_node.left
            node.key = right_min_node.key
            node = right_min_node
            node_parent = right_min_node_parent

        # 要删除的节点是叶子节点或者只有一个子节点
        child = None
        if node.left is not None:
            child = node.left
        elif node.right is not None:
            child = node.right

        # 改变要删除节点的父节点指针指向
        if node_parent is None:
            self.root = child
        elif node_parent.left is node:
            node_parent.left = child
        else:
            node_parent.right = child

    def sorted(self) -> List[int]:
        result = []

        def in_order(root: Optional[TreeNode]):
            if root is None:
                return
            in_order(root.left)
            result.append(root.key)
            in_order(root.right)
        in_order(self.root)
        return result


def test():
    binary_search_tree = BinarySearchTree()
    assert len(binary_search_tree.sorted()) == 0

    # test sorted and insert
    for _ in range(40):
        binary_search_tree = BinarySearchTree()
        for _ in range(10):
            binary_search_tree.insert(randint(1, 10 ** 3))
            result = binary_search_tree.sorted()
            assert list(sorted(result)) == result

    # test delete
    for _ in range(40):
        binary_search_tree = BinarySearchTree()
        for _ in range(10):
            binary_search_tree.insert(randint(1, 10 ** 3))
        result = binary_search_tree.sorted()
        binary_search_tree.delete(choice(result))
        assert list(sorted(result)) == result

    # test find
    for _ in range(40):
        binary_search_tree = BinarySearchTree()
        for _ in range(10):
            binary_search_tree.insert(randint(1, 10 ** 3))
        result = binary_search_tree.sorted()
        assert binary_search_tree.find(choice(result)) is not None
        assert binary_search_tree.find(randint(10 ** 4, 10 ** 6)) is None

    # test operation on empty tree
    binary_search_tree = BinarySearchTree()
    assert binary_search_tree.find(0) is None
    binary_search_tree.insert(0)
    assert binary_search_tree.find(0) is not None
    binary_search_tree.delete(0)
    assert binary_search_tree.find(0) is None
