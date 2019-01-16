package merge_sort_go

func MergeSort(nums []int) []int {
	recursion(nums, 0, len(nums)-1)
	return nums
}

func recursion(nums []int, low, high int) {
	if low < high {
		mid := low + ((high - low) >> 1)
		recursion(nums, low, mid)
		recursion(nums, mid+1, high)
		merge(nums, low, mid, high)
	}
}

func merge(nums []int, low, mid, high int) {
	i, j := low, mid+1
	tmp := make([]int, 0)
	for i <= mid && j <= high {
		if nums[i] < nums[j] {
			tmp = append(tmp, nums[i])
			i += 1
		} else {
			tmp = append(tmp, nums[j])
			j += 1
		}
	}

	if i > mid {
		tmp = append(tmp, nums[j:high+1]...)
	}

	if j > high {
		tmp = append(tmp, nums[i:mid+1]...)
	}

	index := low
	for _, num := range tmp {
		nums[index] = num
		index += 1
	}
}
