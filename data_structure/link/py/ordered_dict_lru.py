# -*- coding:utf-8 -*-

from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.container = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.container:
            return -1
        v = self.container.pop(key)
        self.container[key] = v
        return v

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.container:
            self.container.pop(key)
        else:
            if self.capacity > 0:
                self.capacity -= 1
            else:
                self.container.popitem(last=False)
        self.container[key] = value


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
