
"""
使用前中后遍历一颗完全二叉树，假设二叉树使用数组存储，
从下标1开始，那么左节点：2 * i, 右节点：2 * i + 1
                     1
                   /   \
                  2     3
                /   \  /  \
              4     5 6    7
"""


def pre_order(tree: list, node=1):
    if node > len(tree) - 1:
        return
    print(tree[node], end=' ')
    pre_order(tree, node * 2)
    pre_order(tree, node * 2 + 1)


def in_order(tree: list, node=1):
    if node > len(tree) - 1:
        return
    in_order(tree, node * 2)
    print(tree[node], end=' ')
    in_order(tree, node * 2 + 1)


def post_order(tree: list, node=1):
    if node > len(tree) - 1:
        return
    post_order(tree, node * 2)
    post_order(tree, node * 2 + 1)
    print(tree[node], end=' ')


def level_order(tree: list):
    if len(tree) < 2:
        return
    index = 1
    queue = [tree[index]]
    while len(queue) > 0:
        tmp = []
        while len(queue) > 0:
            print(queue.pop(0), end=' ')
            if index * 2 <= len(tree) - 1:
                tmp.append(tree[index * 2])
            if index * 2 + 1 <= len(tree) - 1:
                tmp.append(tree[index * 2 + 1])
            index += 1
        queue.extend(tmp)


if __name__ == '__main__':
    tree = list(range(0, 8))
    print("前序遍历：")
    pre_order(tree)
    print("\n中序遍历：", end='\n')
    in_order(tree)
    print("\n后序遍历：", end='\n')
    post_order(tree)
    print("\n按层遍历：", end='\n')
    level_order(tree)
