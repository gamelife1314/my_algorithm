# -*- coding:utf-8 -*-

""" 
@author: 付登龙
@file: skip_list.py
@time: 2019/01/13 6:12 PM
"""
from random import randrange, randint, choice
from typing import Optional


class Node(object):

    def __init__(self, key: float=None, next_=None, prev=None, above=None, below=None):
        self.key = key
        self.next = next_
        self.prev = prev
        self.above = above
        self.below = below

    def __repr__(self):
        return f'Node({self.key})'


class SkipList(object):

    MAX_LEVEL = 5

    def __init__(self):
        self.level = -1
        self.start = None
        self.__add_new_level()
        self.__add_new_level()

    def __add_new_level(self):
        head = Node(key=float('-inf'))
        tail = Node(key=float('inf'))
        head.next = tail
        tail.prev = head
        if self.start is None:
            self.start = head
        else:
            p = self.start
            while p.next is not None:
                p = p.next
            self.start.above = head
            head.below = self.start
            p.above = tail
            tail.below = p
            self.start = head
        self.level += 1

    @classmethod
    def __insert_after_above(cls, key: float, p: Node, q: Optional[Node]=None):
        node = Node(key=key, next_=p.next, prev=p, below=q)
        p.next.prev = node
        p.next = node
        if q is not None:
            q.above = node
        return node

    def insert(self, key: float):
        p = self.__search_key(key)
        if p.key == key:
            return  # 已经存在，不做处理
        q = self.__insert_after_above(key, p, None)
        height = 0
        while randrange(2) and height < type(self).MAX_LEVEL - 2:
            height += 1
            if height >= self.level:
                self.__add_new_level()
            while p.above is None:
                p = p.prev
            p = p.above
            q = self.__insert_after_above(key, p, q)

    def __search_key(self, key: float):
        p = self.start
        while p.below is not None:
            p = p.below
            while key >= p.next.key:
                p = p.next
        return p

    def find(self, key: float):
        p = self.__search_key(key)
        return p if p.key == key else None

    def delete(self, key: float):
        p = self.find(key)
        while p is not None:
            p.next.prev = p.prev
            p.prev.next = p.next
            p = p.above

    def sorted(self):
        p = self.start
        while p.below is not None:
            p = p.below
        result = []
        p = p.next
        while p.next is not None:
            result.append(p.key)
            p = p.next
        return result


def test():

    # insert and sorted
    for _ in range(100):
        s = SkipList()
        for _ in range(100):
            s.insert(randint(1, 10 ** 4))
        result = s.sorted()
        assert list(sorted(result)) == result
        key = choice(result)
        assert s.find(key) is not None
        s.delete(key)
        assert s.find(key) is None


if __name__ == '__main__':
    test()
