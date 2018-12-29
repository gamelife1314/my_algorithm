class SmallHeap(object):

    def __init__(self):
        self.data = [-1]

    @property
    def size(self):
        return len(self.data) - 1

    @property
    def top(self):
        return self.data[1]

    def insert(self, item):
        ref = self.data
        ref.append(item)
        index = len(ref) - 1
        while index // 2 > 0 and ref[index] < ref[index // 2]:
            ref[index], ref[index // 2] = ref[index // 2], ref[index]
            index = index // 2

    def pop(self):
        if len(self.data) == 1:
            return None
        top = self.data[1]
        self.data[1] = self.data[-1]
        self.data = self.data[0:-1]
        if len(self.data) > 1:
            self.__heapify(1)
        return top

    def __heapify(self, index, length=None):
        ref = self.data
        length = length or len(self.data)
        while True:
            min_pos = index
            if 2 * index < length and ref[2 * index] < ref[index]:
                min_pos = 2 * index
            if 2 * index + 1 < length and ref[2 * index + 1] < ref[min_pos]:
                min_pos = 2 * index + 1
            if index == min_pos:
                break
            ref[index], ref[min_pos] = ref[min_pos], ref[index]
            index = min_pos


class KthLargest:

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.heap = SmallHeap()
        self.capacity = k
        for num in nums:
            self.add(num)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if self.heap.size < self.capacity:
            self.heap.insert(val)
        elif val > self.heap.top:
            self.heap.pop()
            self.heap.insert(val)
        return self.heap.top


if __name__ == '__main__':
    k = KthLargest(3, [-1, -2, 4, 5, -8, -2])
    print(k.add(3))
    print(k.add(5))
    print(k.add(10))
    print(k.add(9))
    print(k.add(4))

