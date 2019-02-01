package bsearch_go

// 二分查找算法的实现，在有序数组中查找
// 第一个与指定值相等的元素，如果找到返
// 回该值在列表中的下表，如果没有找到返
// 回 -1。

func BsearchFirstEqual(items []int, target int) int {
	low, high := 0, len(items)-1
	for low <= high {
		mid := low + ((high - low) >> 1)
		if items[mid] > target {
			high = mid - 1
		} else if items[mid] < target {
			low = mid + 1
		} else {
			if mid == 0 || items[mid-1] != target {
				return mid
			} else {
				high = mid - 1
			}
		}
	}
	return -1
}

// 二分查找算法的实现，在有序数组中查找
// 最后一个与指定值相等的元素，如果找到返
// 回该值在列表中的下表，如果没有找到返
// 回 -1。
func BsearchLastEqual(items []int, target int) int {
	low, high := 0, len(items)-1
	for low <= high {
		mid := low + ((high - low) >> 1)
		if items[mid] > target {
			high = mid - 1
		} else if items[mid] < target {
			low = mid + 1
		} else {
			if mid == len(items)-1 || items[mid+1] != target {
				return mid
			} else {
				low = mid + 1
			}
		}
	}
	return -1
}

// 二分查找算法的实现，在有序数组中查找
// 第一个小于等于指定值的元素，如果找到返
// 回该值在列表中的下表，如果没有找到返
// 回 -1。
func BsearchFirstLessThan(items []int, target int) int {
	low, high := 0, len(items)-1
	for low <= high {
		mid := low + ((high - low) >> 1)
		if items[mid] > target {
			high = mid - 1
		} else {
			return 0
		}
	}
	return -1
}

// 二分查找算法的实现，在有序数组中查找
// 最后一个小于等于指定值的元素，如果找到返
// 回该值在列表中的下表，如果没有找到返
// 回 -1。
func BsearchLastLessThan(items []int, target int) int {
	low, high := 0, len(items)-1
	for low <= high {
		mid := low + ((high - low) >> 1)
		if items[mid] > target {
			high = mid - 1
		} else {
			if mid == len(items)-1 || items[mid+1] > target {
				return mid
			} else {
				low = mid + 1
			}
		}
	}
	return -1
}

// 二分查找算法的实现，在有序数组中查找
// 第一个大于等于指定值的元素，如果找到返
// 回该值在列表中的下表，如果没有找到返
// 回 -1。
func BsearchFirstGreaterThan(items []int, target int) int {
	low, high := 0, len(items)-1
	for low <= high {
		mid := low + ((high - low) >> 1)
		if items[mid] < target {
			low = mid + 1
		} else {
			if mid == 0 || items[mid-1] < target {
				return mid
			} else {
				high = mid - 1
			}
		}
	}
	return -1
}
