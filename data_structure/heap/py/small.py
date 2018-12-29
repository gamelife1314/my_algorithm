class SmallHeap(object):

    def __init__(self):
        self.data = [-1]

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

    @classmethod
    def from_iterable(cls, iterable):
        h = cls()
        for item in iterable:
            h.insert(item)
        return h


if __name__ == '__main__':
    heap = SmallHeap.from_iterable([4, 5, 8, 2])
    heap.pop()
    heap.insert(10)
    print(heap.data)
