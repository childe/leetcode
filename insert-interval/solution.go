package main

import (
	"fmt"
	"reflect"
)

/*
https://leetcode.com/problems/insert-interval/

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]


Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
*/

func insert(intervals [][]int, newInterval []int) [][]int {
	var (
		l = newInterval[0]
		r = newInterval[1]

		start = 0
		end   = len(intervals) - 1
		mid   = (start + end) / 2

		in = false

		new_left int

		rst = make([][]int, 0)
	)

	for !in && start <= end {
		switch {
		case l < intervals[mid][0]:
			end = mid - 1
			mid = (start + end) / 2
		case l > intervals[mid][1]:
			start = mid + 1
			mid = (start + end) / 2
		default:
			in = true
		}
	}

	if in {
		new_left = intervals[mid][0]
		rst = append(rst, intervals[:mid]...)
	} else {
		new_left = l
		rst = append(rst, intervals[:start]...)
	}

	start = mid
	end = len(intervals) - 1
	mid = (start + end) / 2
	in = false

	for !in && start <= end {
		switch {
		case r < intervals[mid][0]:
			end = mid - 1
			mid = (start + end) / 2
		case r > intervals[mid][1]:
			start = mid + 1
			mid = (start + end) / 2
		default:
			in = true
		}
	}

	if in {
		rst = append(rst, []int{new_left, intervals[mid][1]})
		rst = append(rst, intervals[mid+1:]...)
	} else {
		rst = append(rst, []int{new_left, r})
		rst = append(rst, intervals[start:]...)
	}

	return rst
}

func main() {
	var intervals [][]int
	var newInterval []int
	var rst [][]int

	intervals = [][]int{{1, 3}, {6, 9}}
	newInterval = []int{2, 5}
	rst = insert(intervals, newInterval)
	fmt.Println(rst)
	fmt.Println(reflect.DeepEqual(rst, [][]int{{1, 5}, {6, 9}}))

	intervals = [][]int{{1, 2}, {3, 5}, {6, 7}, {8, 10}, {12, 16}}
	newInterval = []int{4, 8}
	rst = insert(intervals, newInterval)
	fmt.Println(rst)
	fmt.Println(reflect.DeepEqual(rst, [][]int{{1, 2}, {3, 10}, {12, 16}}))

	intervals = [][]int{{1, 5}}
	newInterval = []int{2, 3}
	rst = insert(intervals, newInterval)
	fmt.Println(rst)
	fmt.Println(reflect.DeepEqual(rst, [][]int{{1, 5}}))

	intervals = [][]int{{0, 1}, {2, 6}, {9, 11}}
	newInterval = []int{5, 10}
	rst = insert(intervals, newInterval)
	fmt.Println(rst)
	fmt.Println(reflect.DeepEqual(rst, [][]int{{0, 1}, {2, 11}}))
}
