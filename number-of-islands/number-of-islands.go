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

type P struct {
	x, y int
}

func numIslands(grid [][]byte) int {
	islands := make(map[P]*P)
	for {
		x, y := findUnvisited(grid, islands)
		if x == -1 {
			return len(islands)
		}
		islands[P{x, y}] = &P{x, y}

		// BFS 遍历当前 island
		island_stack := []P{P{x, y}}
		for len(island_stack) > 0 {
			i, j := island_stack[0].x, island_stack[0].y
			island_stack = island_stack[1:]

			// 把上下左右的1都找到
			ps := []P{P{i - 1, j}, P{i + 1, j}, P{i, j - 1}, P{i, j + 1}}
			for _, p := range ps {
				if p.x >= 0 && p.x < len(grid) && p.y >= 0 && p.y < len(grid[p.x]) &&
					!(p.x == x && p.y == y) && grid[p.x][p.y] == '1' {
					grid[p.x][p.y] = '0'
					island_stack = append(island_stack, p)
				}
			}
		}
	}

	return len(islands)
}

func findUnvisited(grid [][]byte, islands map[P]*P) (int, int) {
	for i, row := range grid {
		for j, c := range row {
			if c == '1' && islands[P{i, j}] == nil {
				return i, j
			}
		}
	}
	return -1, -1
}
