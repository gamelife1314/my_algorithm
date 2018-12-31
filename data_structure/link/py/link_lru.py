# -*- coding:utf-8 -*-


class Node(object):

    def __init__(self, key, value, next_=None, prev=None):
        self.key = key
        self.value = value
        self.next = next_
        self.prev = prev

    def __repr__(self):
        return f'Node({self.key!r}, {self.value!r})'


class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.head = Node('head', 'head')
        self.recorder = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.recorder:
            return -1

        node = self.recorder[key]
        node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.next = self.head.next
        if self.head.next is not None:
            self.head.next.prev = node
        self.head.next = node
        node.prev = self.head
        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.recorder:
            node = self.recorder[key]
            node.prev.next = node.next
            if node.next is not None:
                node.next.prev = node.prev
            del self.recorder[key]
        else:
            if self.capacity > 0:
                self.capacity -= 1
            else:
                move = self.head.next
                while move.next is not None:
                    move = move.next
                move.prev.next = None
                move.prev = None
                del self.recorder[move.key]

        node = Node(key, value, self.head.next, prev=self.head)
        if self.head.next is not None:
            self.head.next.prev = node
        self.head.next = node
        self.recorder[key] = node

    def __repr__(self):
        move = self.head.next
        result = ''
        while move is not None:
            result += str(move.key)
            move = move.next
        return result


def test():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1
    cache.put(4, 4)
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4


if __name__ == '__main__':
    test()
