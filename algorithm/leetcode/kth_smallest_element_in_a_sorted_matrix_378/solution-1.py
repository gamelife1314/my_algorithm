class Heap:

    def __init__(self, capacity):
        self.capacity = capacity
        self.c = [None] * capacity
        self.index = -1

    def insert(self, item):
        self.index += 1
        self.c[self.index] = item
        index = self.index
        root = (self.index - 1) // 2
        while root >= 0 and self.c[index] < self.c[root]:
            self.c[root], self.c[index] = self.c[index], self.c[root]
            index = root
            root = (index - 1) // 2

    def pop(self):
        value = self.c[0]
        self.c[0] = self.c[self.index]
        self.index -= 1
        self.heapify(self.c, self.index + 1, 0)
        return value

    @staticmethod
    def heapify(nums, length, i):
        while True:
            min_pos, left, right = i, 2 * i + 1, 2 * i + 2
            if left < length and nums[left] <= nums[min_pos]:
                min_pos = left
            if right < length and nums[right] <= nums[min_pos]:
                min_pos = right
            if min_pos == i:
                break
            nums[min_pos], nums[i] = nums[i], nums[min_pos]
            i = min_pos


class Solution:

    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        heap = Heap(len(matrix) ** 2 - k + 1)
        for line in matrix:
            for num in line:
                if heap.index < heap.capacity - 1:
                    heap.insert(num)
                else:
                    if num >= heap.c[0]:
                        heap.pop()
                        heap.insert(num)
        return heap.c[0]


if __name__ == '__main__':
    m = [
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15]
    ]
    s = Solution()
    print(s.kthSmallest(m, 1))
