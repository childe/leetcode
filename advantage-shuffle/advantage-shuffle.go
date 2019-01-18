package main

import (
	"fmt"
	"sort"
)

/*
https://leetcode.com/problems/advantage-shuffle/

870. Advantage Shuffle
Medium

204

15

Favorite

Share
Given two arrays A and B of equal size, the advantage of A with respect to B is the number of indices i for which A[i] > B[i].

Return any permutation of A that maximizes its advantage with respect to B.



Example 1:

Input: A = [2,7,11,15], B = [1,10,4,11]
Output: [2,11,7,15]
Example 2:

Input: A = [12,24,8,32], B = [13,25,32,11]
Output: [24,32,8,12]


Note:

1 <= A.length = B.length <= 10000
0 <= A[i] <= 10^9
0 <= B[i] <= 10^9
*/

type BB struct {
	b   int
	idx int
}

func advantageCount(A []int, B []int) []int {
	rst := make([]int, len(A))

	bbs := make([]BB, len(B))
	for i, b := range B {
		bbs[i] = BB{b, i}
	}
	sort.Slice(bbs, func(i, j int) bool { return bbs[i].b < bbs[j].b })
	sort.Ints(A)

	left, right := 0, len(A)-1
	for _, a := range A {
		if a > bbs[left].b {
			rst[bbs[left].idx] = a
			left++
		} else {
			rst[bbs[right].idx] = a
			right--
		}
	}

	return rst
}

func main() {
	A := []int{12, 24, 8, 32}
	B := []int{13, 25, 32, 11}
	A = advantageCount(A, B)
	fmt.Println(A)
}
