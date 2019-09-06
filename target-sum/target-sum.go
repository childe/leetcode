package main

/*
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3.
Output: 5

Explanation:
-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
*/

func findTargetSumWays(nums []int, S int) int {
	if len(nums) == 0 {
		return 0
	}
	if len(nums) == 1 {
		rst := 0
		if nums[0] == S {
			rst++
		}
		if nums[0] == -S {
			rst++
		}
		return rst
	}

	return findTargetSumWays(nums[1:], S-nums[0]) + findTargetSumWays(nums[1:], S+nums[0])
}

func main() {
	print(findTargetSumWays([]int{1, 0}, 1))
}
