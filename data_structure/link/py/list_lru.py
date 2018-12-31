# -*- coding:utf-8 -*-


class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.keys = []
        self.values = []

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.keys:
            return -1

        index = self.keys.index(key)
        value = self.values[index]
        self.keys.remove(key)
        self.values.pop(index)
        self.keys.append(key)
        self.values.append(value)
        return value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """

        if key in self.keys:
            index = self.keys.index(key)
            self.keys.remove(key)
            self.values.pop(index)
        else:
            if self.capacity > 0:
                self.capacity -= 1
            else:
                self.keys.pop(0)
                self.values.pop(0)

        self.keys.append(key)
        self.values.append(value)


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
