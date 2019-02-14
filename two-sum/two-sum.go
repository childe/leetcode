package main

import (
	"fmt"
	"sort"
)

func index(nums []int, n int) int {
	for idx, v := range nums {
		if n == v {
			return idx
		}
	}
	return -1
}

func reverseIndex(nums []int, n int) int {
	for idx := len(nums) - 1; idx >= 0; idx-- {
		if nums[idx] == n {
			return idx
		}
	}
	return -1
}

func twoSum(nums []int, target int) []int {
	sorted := make([]int, len(nums))
	copy(sorted, nums)

	sort.Ints(sorted)
	i, j, s := 0, len(sorted)-1, 0
	for {
		switch s = sorted[i] + sorted[j]; {
		case s == target:
			return []int{index(nums, sorted[i]), reverseIndex(nums, sorted[j])}
		case s > target:
			j--
		case s < target:
			i++
		}
	}

	return nil
}

func main() {
	res := twoSum([]int{1, 2, 3}, 4)
	fmt.Println(res)
	res = twoSum([]int{3, 3}, 6)
	fmt.Println(res)
}
