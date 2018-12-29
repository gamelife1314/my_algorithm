import heapq


class KthLargest:

    def __init__(self, k, nums):
        self.capacity = k
        heapq.heapify(nums)
        self.nums = nums
        while len(self.nums) > self.capacity:
            heapq.heappop(self.nums)

    def add(self, val):
        if len(self.nums) < self.capacity:
            heapq.heappush(self.nums, val)
        elif val > self.nums[0]:
            heapq.heapreplace(self.nums, val)
        return self.nums[0]
