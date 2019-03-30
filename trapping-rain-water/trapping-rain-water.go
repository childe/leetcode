package main

import "fmt"

/*
https://leetcode.com/problems/trapping-rain-water/

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
*/

func trap(height []int) int {
	var (
		c    int
		cACC []int = make([]int, len(height))
		left int
		len  int = len(height)
		i    int
	)

	for left = 0; left < len && height[left] == 0; left++ {
	}

	for i < len-1 {
		cACC[left] = 0
		mostHeight := left + 1
		found := false

		for i = left + 1; i < len; i++ {
			if height[i] >= height[left] {
				found = true
				break
			}
			if height[i] >= height[mostHeight] {
				mostHeight = i
			}
			cACC[i] = cACC[i-1] + height[left] - height[i]
		}
		if found {
			//fmt.Println(cACC)
			c += cACC[i-1]
			left = i
		} else {
			c += cACC[mostHeight] - (height[left]-height[mostHeight])*(mostHeight-left)
			left = mostHeight
			i = left
		}
	}

	return c
}

func main() {
	var height []int
	var c int

	height = []int{}
	c = trap(height)
	fmt.Printf("%d %v\n", c, c == 0)

	height = []int{2}
	c = trap(height)
	fmt.Printf("%d %v\n", c, c == 0)

	height = []int{2, 0, 1}
	c = trap(height)
	fmt.Printf("%d %v\n", c, c == 1)

	height = []int{2, 1, 1}
	c = trap(height)
	fmt.Printf("%d %v\n", c, c == 0)

	height = []int{2, 0, 1, 2}
	c = trap(height)
	fmt.Printf("%d %v\n", c, c == 3)

	height = []int{2, 0, 1, 1}
	c = trap(height)
	fmt.Printf("%d %v\n", c, c == 1)

	height = []int{2, 1}
	c = trap(height)
	fmt.Printf("%d %v\n", c, c == 0)

	height = []int{0, 1, 0, 2}
	c = trap(height)
	fmt.Printf("%d %v\n", c, c == 1)

	height = []int{0, 1, 2, 3}
	c = trap(height)
	fmt.Printf("%d %v\n", c, c == 0)

	height = []int{2, 2, 2, 2}
	c = trap(height)
	fmt.Printf("%d %v\n", c, c == 0)

	height = []int{0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1}
	c = trap(height)
	fmt.Printf("%d %v\n", c, c == 6)
}
