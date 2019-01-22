# -*- coding:utf-8 -*-

"""
从数组下标为0开始存储数据
@author: 付登龙
@file: big-1.py
@time: 2019/01/17 10:50 PM
"""


class BigHeap(object):

    def __init__(self):
        self.data = []

    def insert(self, item: int):
        self.data.append(item)
        index = len(self.data) - 1
        root = (index - 1) >> 1
        while root >= 0 and self.data[index] > self.data[root]:
            self.data[root], self.data[index] = self.data[index], self.data[root]
            index = root
            root = (index - 1) >> 1

    def pop(self):
        if len(self.data) > 0:
            value = self.data[0]
            self.data[0] = self.data[-1]
            self.data = self.data[0:-1]
            root, length = 0, len(self.data)
            while True:
                max_pos, left, right = root, 2 * root + 1, 2 * root + 2
                if left < length and self.data[left] > self.data[max_pos]:
                    max_pos = left
                if right < length and self.data[right] > self.data[max_pos]:
                    max_pos = right
                if max_pos == root:
                    break
                self.data[root], self.data[max_pos] = self.data[max_pos], self.data[root]
                root = max_pos
            return value


if __name__ == '__main__':
    heap = BigHeap()
    for i in range(10):
        heap.insert(i)
    while True:
        pop = heap.pop()
        if pop is None:
            break
        else:
            print(pop, end=" ")