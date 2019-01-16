package insert_sort_go

func InsertSort(nums []int) []int {
	length := len(nums)
	if length > 2 {
		for i := 1; i < length; i++ {
			value := nums[i]
			j := i - 1
			for j >= 0 {
				if nums[j] > value {
					nums[j+1] = nums[j]
					j -= 1
				} else {
					break
				}
			}
			nums[j+1] = value
		}
	}
	return nums
}
