package main

import (
	"fmt"
	"strings"
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

func solveNQueens(n int) [][]string {
	var (
		i        = 0
		j        = 0
		solution []int
		rst      = make([][]string, 0)
	)

	for {
		solution = make([]int, n)
		for i < n {
			for j = solution[i] + 1; j <= n; j++ {
				fmt.Printf("%v %d %d\n", solution, i, j)
				if ifValid(solution, i, j) {
					fmt.Println("valid")
					solution[i] = j
					break
				}
				fmt.Println("not valid")
			}
			fmt.Printf("j = %d\n", j)

			if j > n {
				if i == 0 {
					return rst
				}

				solution[i] = 0
				i--
			} else {
				i++
				if i == n {
					rst = append(rst, solutionToString(solution))
				}
			}
		}
	}

	return rst
}

func solutionToString(solution []int) []string {
	rst := make([]string, len(solution))
	for i, n := range solution {
		b := make([]byte, n)
		for j, _ := range b {
			b[j] = '.'
		}
		b[n-1] = 'Q'
		rst[i] = string(b)
	}
	return rst
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

func conv(s []string) []int {
	rst := make([]int, len(s))
	for i, str := range s {
		rst[i] = strings.Index(str, "Q")
	}
	return rst
}

func check(s []int) bool {
	for i, n := range s {
		for j := 0; j < i; j++ {
			if s[j] == n {
				return false
			}
			if n-s[j] == j-i {
				return false
			}
			if n-s[j] == i-j {
				return false
			}
		}
	}
	return true
}

func main() {
	var n int
	var rst [][]string
	n = 4
	rst = solveNQueens(n)
	fmt.Println(rst)
	fmt.Println(len(rst) == 2)

	//one := []string{"..Q.", "Q...", "...Q", ".Q.."}
	//fmt.Println(check(conv(one)))
}
