package bubble_sort_go

func BubbleSort(nums []int) []int {
	length := len(nums)
	if length > 1 {
		for i := 0; i < length; i++ {
			for j := 0; j < length-i-1; j++ {
				if nums[j+1] < nums[j] {
					nums[j], nums[j+1] = nums[j+1], nums[j]
				}
			}
		}
	}
	return nums
}
