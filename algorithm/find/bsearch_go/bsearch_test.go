package bsearch_go

import "testing"

func TestBsearchFirstEqual(t *testing.T) {
	nums := []int{1, 1}
	if BsearchFirstEqual(nums, 1) != 0 {
		t.Fatalf("1 在 %v 中第一次出现的位置应该是：0", nums)
	}
	nums = []int{1, 2, 2, 3, 4}
	if BsearchFirstEqual(nums, 2) != 1 {
		t.Fatalf("2 在 %v 中第一次出现的位置应该是：1", nums)
	}
	if BsearchFirstEqual(nums, 3) != 3 {
		t.Fatalf("3 在 %v 中第一次出现的位置应该是：3", nums)
	}
	if BsearchFirstEqual(nums, 4) != 4 {
		t.Fatalf("4 在 %v 中第一次出现的位置应该是：4", nums)
	}
}

func TestBsearchLastEqual(t *testing.T) {
	nums := []int{1, 1}
	if BsearchLastEqual(nums, 1) != 1 {
		t.Fatalf("1 在 %v 中最后一次出现的位置应该是：1", nums)
	}
	nums = []int{1, 2, 2, 3, 4}
	if BsearchLastEqual(nums, 2) != 2 {
		t.Fatalf("2 在 %v 中最后一次出现的位置应该是：2", nums)
	}
	if BsearchLastEqual(nums, 3) != 3 {
		t.Fatalf("3 在 %v 中最后一次出现的位置应该是：3", nums)
	}
	if BsearchLastEqual(nums, 4) != 4 {
		t.Fatalf("4 在 %v 中最后一次出现的位置应该是：4", nums)
	}
}

func TestBsearchFirstLessThan(t *testing.T) {
	nums := []int{1, 1}
	if BsearchFirstLessThan(nums, 1) != 0 {
		t.Fatalf("%v 中第一个小于等于1的应该是：0", nums)
	}
	nums = []int{1, 2, 2, 3, 4}
	if BsearchFirstLessThan(nums, 2) != 0 {
		t.Fatalf("%v 中第一个小于等于2的应该是：0", nums)
	}
	if BsearchFirstLessThan(nums, 3) != 0 {
		t.Fatalf("%v 中第一个小于等于3的应该是：0", nums)
	}
	if BsearchFirstLessThan(nums, 4) != 0 {
		t.Fatalf("%v 中第一个小于等于4的应该是：0", nums)
	}
	if BsearchFirstLessThan(nums, 0) != -1 {
		t.Fatalf("%v 中第一个小于等于0的应该是：-1", nums)
	}
}

func TestBsearchLastLessThan(t *testing.T) {
	nums := []int{1, 1}
	if BsearchLastLessThan(nums, 1) != 1 {
		t.Fatalf("%v 中最后一个小于等于1的应该是：1", nums)
	}
	nums = []int{1, 2, 2, 3, 4}
	if BsearchLastLessThan(nums, 2) != 2 {
		t.Fatalf("%v 中最后一个小于等于2的应该是：2", nums)
	}
	if BsearchLastLessThan(nums, 3) != 3 {
		t.Fatalf("%v 中最后一个小于等于3的应该是：3", nums)
	}
	if BsearchLastLessThan(nums, 4) != 4 {
		t.Fatalf("%v 中最后一个小于等于4的应该是：4", nums)
	}
	if BsearchLastLessThan(nums, 5) != 4 {
		t.Fatalf("%v 中最后一个小于等于5的应该是：4", nums)
	}
	if BsearchLastLessThan(nums, 0) != -1 {
		t.Fatalf("%v 中最后一个小于等于0的应该是：-1", nums)
	}
}

func TestBsearchFirstGreaterThan(t *testing.T) {
	nums := []int{1, 1}
	if BsearchFirstGreaterThan(nums, 1) != 0 {
		t.Fatalf("%v 中第一个大于等于1的应该是：0", nums)
	}
	nums = []int{1, 2, 2, 3, 4}
	if BsearchFirstGreaterThan(nums, 2) != 1 {
		t.Fatalf("%v 中第一个大于等于2的应该是：1", nums)
	}
	if BsearchFirstGreaterThan(nums, 3) != 3 {
		t.Fatalf("%v 中第一个大于等于3的应该是：3", nums)
	}
	if BsearchFirstGreaterThan(nums, 4) != 4 {
		t.Fatalf("%v 中第一个大于等于4的应该是：4", nums)
	}
	if BsearchFirstGreaterThan(nums, 5) != -1 {
		t.Fatalf("%v 中第一个大于等于于5的应该是：-1", nums)
	}
	if BsearchFirstGreaterThan(nums, 0) != 0 {
		t.Fatalf("%v 中第一个大于等于0的应该是：0", nums)
	}
}
