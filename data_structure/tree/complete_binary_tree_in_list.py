"""
使用前中后遍历二叉树
"""
from typing import Optional


class TreeNode(object):

    __slots__ = ('data', 'left', 'right')

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Tree(object):

    def __init__(self, root: Optional[TreeNode]=None):
        self.root = root

    @classmethod
    def from_array(cls, items: list):
        length = len(items)
        if length < 2:
            return cls()
        nodes = [TreeNode(items[i]) for i in range(length)]
        for i in range(1, length):
            if 2 * i < length:
                nodes[i].left = nodes[2 * i]
            if 2 * i + 1 < length:
                nodes[i].right = nodes[2 * i + 1]
        return cls(nodes[1])

    def pre_order(self, root: Optional[TreeNode]=None):
        if root is None:
            return
        print(root.data, end=' ')
        self.pre_order(root.left)
        self.pre_order(root.right)

    def in_order(self, root: Optional[TreeNode]=None):
        if root is None:
            return
        self.in_order(root.left)
        print(root.data, end=' ')
        self.in_order(root.right)

    def post_order(self, root: Optional[TreeNode]=None):
        if root is None:
            return
        self.post_order(root.left)
        self.post_order(root.right)
        print(root.data, end=' ')

    def level_order(self):
        if self.root is None:
            return
        queue = [self.root]
        while len(queue) > 0:
            tmp = []
            while len(queue) > 0:
                node = queue.pop(0)
                print(node.data, end=' ')
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            queue.extend(tmp)


if __name__ == '__main__':
    tree = Tree.from_array(items=list(range(0, 8)))
    print("前序遍历：")
    tree.pre_order(tree.root)
    print("\n中序遍历：")
    tree.in_order(tree.root)
    print("\n后序遍历：")
    tree.post_order(tree.root)
    print("\n层次遍历：")
    tree.level_order()
