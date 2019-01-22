package heap_sort_go

func HeapSort(nums []int) {
	length := len(nums)
	buildHeap(nums, length)
	for i := length - 1; i > 0; i-- {
		nums[0], nums[i] = nums[i], nums[0]
		heapify(nums, i, 0)
	}
}

func buildHeap(nums []int, length int) {
	for i := (length - 2) >> 1; i >= 0; i-- {
		heapify(nums, length, i)
	}
}

func heapify(nums []int, length, start int) {
	for {
		maxPos, left, right := start, 2*start+1, 2*start+2
		if left < length && nums[left] > nums[maxPos] {
			maxPos = left
		}
		if right < length && nums[right] > nums[maxPos] {
			maxPos = right
		}
		if maxPos == start {
			break
		}
		nums[maxPos], nums[start] = nums[start], nums[maxPos]
		start = maxPos
	}
}
