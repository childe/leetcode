package main

/*

https://leetcode.com/problems/number-of-islands/

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1

Example 2:

Input:
11000
11000
00100
00011

Output: 3
*/

func numIslands(grid [][]byte) int {
	visited := make([][]byte, len(grid))
	for i, _ := range visited {
		visited[i] = make([]byte, len(grid[i]))
		for j, _ := range visited[i] {
			visited[i][j] = 0
		}
	}

	rst := 0
	for {
		i, j := findUnvisited(grid, visited)
		if i == -1 {
			return rst
		}

		rst++

		visited[i][j] = 1

		// BFS 遍历当前 island
		island_stack := [][]int{[]int{i, j}}
		for len(island_stack) > 0 {
			i = island_stack[0][0]
			j = island_stack[0][1]
			island_stack = island_stack[1:]

			// 把上下左右的1都找到
			keys := make([][]int, 0)
			// 上
			if i > 0 && j < len(grid[i-1]) && grid[i-1][j] == 1 && 0 == visited[i-1][j] {
				keys = append(keys, keyGen(i-1, j))
			}
			// 下
			if i < len(grid)-1 && j < len(grid[i+1]) && grid[i+1][j] == 1 && 0 == visited[i+1][j] {
				keys = append(keys, keyGen(i+1, j))
			}

			// 左
			if j > 0 && grid[i][j-1] == 1 && 0 == visited[i][j-1] {
				keys = append(keys, keyGen(i, j-1))
			}

			// 右
			if j < len(grid[i])-1 && grid[i][j+1] == 1 && 0 == visited[i][j+1] {
				keys = append(keys, keyGen(i, j+1))
			}

			for _, key := range keys {
				visited[key[0]][key[1]] = 1
				island_stack = append(island_stack, key)
			}
		}
	}

	return rst
}

func keyGen(i, j int) []int {
	return []int{i, j}
}

func findUnvisited(grid, visited [][]byte) (int, int) {
	for i, row := range grid {
		for j, c := range row {
			if c == 1 && 0 == visited[i][j] {
				return i, j
			}
		}
	}

	return -1, -1
}
