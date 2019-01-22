package merge_sort_go

import (
	"math/rand"
	"sort"
	"testing"
	"time"
)

func compareIntSlice(items1, items2 []int) bool {
	length := len(items2)
	if len(items1) != length {
		return false
	}
	for i := 0; i < length; i++ {
		if items1[i] != items2[i] {
			return false
		}
	}
	return true
}

func TestSort(t *testing.T) {
	for i := 0; i < 100; i++ {
		rand.Seed(time.Now().UnixNano())
		length := rand.Intn(10000)
		if length > 0 {
			t.Logf("数组长度是 %d", length)
			nums := make([]int, length)
			for j := 0; j < length; j++ {
				nums[j] = rand.Intn(100000)
			}
			numsCopy := make([]int, length)
			copy(numsCopy, nums)
			if !compareIntSlice(numsCopy, nums) {
				t.Fatalf("这里不应该有错误")
			}
			sort.Ints(nums)
			MergeSort(numsCopy)
			if !compareIntSlice(numsCopy, nums) {
				t.Fatalf("两个数组应该是相等的才对")
			}
		}
	}
}
