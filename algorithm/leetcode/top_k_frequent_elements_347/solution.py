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
        while root >= 0 and self.c[index][1] > self.c[root][1]:
            self.c[index], self.c[root] = self.c[root], self.c[index]
            index = root

    def pop(self):
        value = self.c[0]
        self.c[0] = self.c[self.index]
        self.index -= 1
        self.heapify(self.c, self.index + 1, 0)
        return value

    @staticmethod
    def heapify(items: list, length, i):
        while True:
            max_pos, left, right = i, 2 * i + 1, 2 * i + 2
            if left < length and items[left][1] > items[max_pos][1]:
                max_pos = left
            if right < length and items[right][1] > items[max_pos][1]:
                max_pos = right
            if max_pos == i:
                break
            items[i], items[max_pos] = items[max_pos], items[i]
            i = max_pos

    @classmethod
    def from_array(cls, items: list):
        length = len(items)
        for i in range((length - 2) >> 1, -1, -1):
            cls.heapify(items, length, i)
        instance = cls(length)
        instance.c = items
        instance.index = length - 1
        return instance


class Solution:

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        heap = Heap.from_array(list(counts.items()))
        return [heap.pop()[0] for _ in range(k)]


if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequent([2], 1))
