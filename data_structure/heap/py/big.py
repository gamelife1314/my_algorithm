class BigHeap(object):

    __slots__ = ('data', )

    def __init__(self):
        self.data = [-1]

    @property
    def size(self):
        return len(self.data) - 1

    def insert(self, item):
        self.data.append(item)
        index = len(self.data) - 1
        r = self.data
        # 自下往上堆化
        while index // 2 > 0 and r[index] > r[index // 2]:
            r[index], r[index // 2] = r[index // 2], r[index]
            index = index // 2

    def pop(self):
        if len(self.data) <= 0:
            return None
        top = self.data[1]
        self.data[1] = self.data[-1]
        self.data = self.data[0:-1]
        if len(self.data) > 1:
            self.__heapify(1)
        return top

    def __heapify(self, index, length=None):
        ref = self.data
        length = length or len(ref)
        # 从上往下进行堆化
        while True:
            max_pos = index
            if 2 * index < length and ref[index] < ref[2 * index]:
                max_pos = 2 * index
            if 2 * index + 1 < length and ref[max_pos] < ref[2 * index + 1]:
                max_pos = 2 * index + 1
            if max_pos == index:
                break
            ref[index], ref[max_pos] = ref[max_pos], ref[index]
            index = max_pos

    @classmethod
    def from_iterable(cls, iterable):
        h = cls()
        for item in iterable:
            h.insert(item)
        return h


if __name__ == '__main__':
    heap = BigHeap.from_iterable([4, 5, 8, 2])
    heap.pop()
    heap.insert(10)
    print(heap.data)

