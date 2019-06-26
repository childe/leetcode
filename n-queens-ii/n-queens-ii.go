package main

import (
	"fmt"
)

/*
Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.

*/

func totalNQueens(n int) int {
	var (
		i        = 0
		j        = 0
		solution []int
		total    int
	)

	for {
		solution = make([]int, n)
		for i < n {
			for j = solution[i] + 1; j <= n; j++ {
				//fmt.Printf("%v %d %d\n", solution, i, j)
				if ifValid(solution, i, j) {
					//fmt.Println("valid")
					solution[i] = j
					break
				}
				//fmt.Println("not valid")
			}
			//fmt.Printf("j = %d\n", j)

			if j > n {
				if i == 0 {
					return total
				}

				solution[i] = 0
				i--
			} else {
				if i+1 == n {
					total++
				} else {
					i++
				}
			}
		}
	}

	return total
}

func ifValid(s []int, i, j int) bool {
	for k := 0; k < i; k++ {
		switch {
		case j == s[k]:
			return false
		case j-s[k] == i-k:
			return false
		case j-s[k] == k-i:
			return false
		}
	}
	return true
}

func main() {
	var n int
	var total int
	n = 14
	total = totalNQueens(n)
	fmt.Println(total)
}
