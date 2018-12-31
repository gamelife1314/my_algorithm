class SmallHeap(object):

    def __init__(self):
        self.data = [-1]

    def insert(self, item):
        ref = self.data
        ref.append(item)
        index = len(ref) - 1
        root = index // 2
        while root > 0 and ref[index] < ref[root]:
            ref[index], ref[root] = ref[root], ref[index]
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
        length = length or len(self.data)
        while True:
            min_pos, left, right = index, 2 * index, 2 * index + 1
            if left < length and ref[left] < ref[index]:
                min_pos = left
            if right < length and ref[right] < ref[min_pos]:
                min_pos = right
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


def heapify(nums):
    length = len(nums)
    for index in reversed(range(0, length // 2)):
        start_pos = index
        while True:
            min_pos, left, right = start_pos, 2 * index + 1, 2 * index + 2
            if left < length and nums[left] < nums[index]:
                min_pos = left
            if right < length and nums[right] < nums[min_pos]:
                min_pos = right
            if min_pos == start_pos:
                break
            nums[start_pos], nums[min_pos] = nums[min_pos], nums[start_pos]
            start_pos = min_pos


if __name__ == '__main__':
    from copy import deepcopy
    import heapq
    nums = [4, 5, 8, 2, 1, 67, 34, 94, -23, -12, 45, -229, 24]
    nums_copy = deepcopy(nums)
    heap = SmallHeap.from_iterable(nums)
    print(heap.data[1:])
    heapq.heapify(nums)
    print(nums)
    heapify(nums_copy)
    print(nums_copy)

