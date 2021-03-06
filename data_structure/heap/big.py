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
        root = index // 2
        while root > 0 and r[index] > r[root]:
            r[index], r[root] = r[root], r[index]
            index = root
            root = index // 2

    def pop(self):
        if len(self.data) < 2:
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
            max_pos, left, right = index, 2 * index, 2 * index + 1
            if left < length and ref[index] < ref[left]:
                max_pos = left
            if right < length and ref[max_pos] < ref[right]:
                max_pos = right
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

