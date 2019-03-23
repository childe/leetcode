package main

import "fmt"

/*
https://leetcode.com/problems/first-missing-positive/

Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3

Example 2:

Input: [3,4,-1,1]
Output: 2

Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.
*/

/*
目标数据应该 <= length+1, 比如 nums 是 [1,2,3,4] , 那目标数据是5. 如果nums没有这么紧密, 目标数据应该比5更小
1. 预处理一下, 把所有非正数和大于length的数字去掉
2. 先找到 >0 && <=length 的数字. 然后把数字i插入到nums[i]
3. 遍历, 找到第一个没被插入的数字
*/

func firstMissingPositive(nums []int) int {
	length := len(nums)
	for i, n := range nums {
		if n <= 0 || n > length {
			nums[i] = 0
		}
	}

	for _, n := range nums {
		if n > length {
			n -= (length + 1)
		}
		if n == 0 {
			continue
		}
		if nums[n-1] < length+1 {
			nums[n-1] += (length + 1)
		}
	}

	for i, n := range nums {
		if n <= length {
			return i + 1
		}
	}
	return length + 1
}

func main() {
	var nums []int
	var answer int
	nums = []int{1, 2, 0}
	answer = firstMissingPositive(nums)
	fmt.Printf("%v %d\n", 3 == answer, answer)

	nums = []int{3, 4, -1, 1}
	answer = firstMissingPositive(nums)
	fmt.Printf("%v %d\n", 2 == answer, answer)

	nums = []int{7, 8, 9, 11, 12}
	answer = firstMissingPositive(nums)
	fmt.Printf("%v %d\n", 1 == answer, answer)

	nums = []int{1, 2, 3, 4}
	answer = firstMissingPositive(nums)
	fmt.Printf("%v %d\n", 5 == answer, answer)

	nums = []int{1, 1, 1, 1}
	answer = firstMissingPositive(nums)
	fmt.Printf("%v %d\n", 2 == answer, answer)

	nums = []int{0, 0, 0, 0}
	answer = firstMissingPositive(nums)
	fmt.Printf("%v %d\n", 1 == answer, answer)

	nums = []int{-1, -1, -1, -1}
	answer = firstMissingPositive(nums)
	fmt.Printf("%v %d\n", 1 == answer, answer)

	nums = []int{3, 3, 1, 4, 0}
	answer = firstMissingPositive(nums)
	fmt.Printf("%v %d\n", 2 == answer, answer)

	nums = []int{}
	answer = firstMissingPositive(nums)
	fmt.Printf("%v %d\n", 1 == answer, answer)
}
