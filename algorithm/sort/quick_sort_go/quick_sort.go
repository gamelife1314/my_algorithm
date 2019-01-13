package quick_sort_go

func Sort(nums []int) []int {
	recursion(nums, 0, len(nums)-1)
	return nums
}

func recursion(nums []int, low, high int) {
	if low < high {
		point := partition(nums, low, high)
		recursion(nums, low, point-1)
		recursion(nums, point+1, high)
	}
}

func partition(nums []int, low, high int) int {
	pivot := nums[high]
	i := low
	for j := low; j <= high-1; j++ {
		if nums[j] < pivot {
			nums[i], nums[j] = nums[j], nums[i]
			i += 1
		}
	}
	nums[i], nums[high] = nums[high], nums[i]
	return i
}
