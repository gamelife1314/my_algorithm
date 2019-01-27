# -*- coding:utf-8 -*-


class Heap:

    def __init__(self, capacity):
        self.capacity = capacity
        self.c = [None] * self.capacity
        self.index = -1

    def insert(self, item):
        self.index += 1
        self.c[self.index] = item
        index = self.index
        root = (index - 1) // 2
        while root >= 0 and self.c[index] < self.c[root]:
            self.c[index], self.c[root] = self.c[root], self.c[index]
            index = root
            root = (index - 1) // 2

    def pop(self):
        value = self.c[0]
        self.c[0] = self.c[self.index]
        self.index -= 1
        self.heapify(self.c, self.index + 1, 0)
        return value

    @staticmethod
    def heapify(nums: list, length, start):
        while True:
            min_pos, left, right = start, 2 * start + 1, 2 * start + 2
            if left < length and nums[left] < nums[min_pos]:
                min_pos = left
            if right < length and nums[right] < nums[min_pos]:
                min_pos = right
            if min_pos == start:
                break
            nums[min_pos], nums[start] = nums[start], nums[min_pos]
            start = min_pos


class Solution:

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = Heap(k)
        for num in nums:
            if heap.index < k - 1:
                heap.insert(num)
            else:
                if num >= heap.c[0]:
                    heap.pop()
                    heap.insert(num)
        return heap.c[0]


if __name__ == '__main__':
    s = Solution()
    print(s.findKthLargest([3, 2, 1, 5, 6, 4], 2))
    s = Solution()
    print(s.findKthLargest([7, 6, 5, 4, 3, 2, 1], 5))

