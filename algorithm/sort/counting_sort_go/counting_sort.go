package counting_sort_go

func max(nums []int) int {
	maxNum := nums[0]
	for i := 1; i < len(nums); i++ {
		if nums[i] > maxNum {
			maxNum = nums[i]
		}
	}
	return maxNum
}

func CountingSort(nums []int) []int {
	length := len(nums)
	if length > 1 {
		maxNum := max(nums)
		buckets := make([]int, maxNum+1)

		// 计数
		for _, num := range nums {
			buckets[num] += 1
		}

		// 累加
		for i := 1; i < maxNum+1; i++ {
			buckets[i] = buckets[i] + buckets[i-1]
		}

		// 排序
		tmp := make([]int, length)
		for _, num := range nums {
			index := buckets[num] - 1
			tmp[index] = num
			buckets[num] -= 1
		}
		return tmp
	}
	return nums
}
