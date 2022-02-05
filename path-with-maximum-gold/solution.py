#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/problems/path-with-maximum-gold/

1219. Path with Maximum Gold

In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

Every time you are located in a cell you will collect all the gold in that cell.
From your position, you can walk one step to the left, right, up, or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.
 

Example 1:

Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
Explanation:
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7.
Example 2:

Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
Output: 28
Explanation:
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 15
0 <= grid[i][j] <= 100
There are at most 25 cells containing gold.
"""


class Solution:
    def getMaximumGold(self, grid: list[list[int]]) -> int:
        """
        >>> solution = Solution()
        >>> solution.getMaximumGold([[0,6,0],[5,8,7],[0,9,0]])
        24
        >>> solution.getMaximumGold([[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]])
        28
        """
        ans = 0
        m, n = len(grid), len(grid[0])

        def dfs(x, y, gold_sum):
            # print(grid, x, y, gold_sum)
            nonlocal ans
            backup = grid[x][y]
            grid[x][y] = 0
            ans = max(ans, gold_sum + backup)
            # print(f"{ans=}")
            for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                if grid[nx][ny] == 0:
                    continue
                dfs(nx, ny, gold_sum + backup)
            grid[x][y] = backup

        candidates = []
        for x in range(m):
            for y in range(n):
                count = 0
                for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if nx < 0 or nx >= m or ny < 0 or ny >= n:
                        continue
                    if grid[nx][ny] > 0:
                        count += 1
                    if count > 0:
                        break

                if count == 1:
                    candidates.append((x, y))

        for x, y in candidates:
            dfs(x, y, 0)
        return ans


def main():
    solution = Solution()
    ans = solution.getMaximumGold([[0, 6, 0], [5, 8, 7], [0, 9, 0]])
    print(ans)


if __name__ == "__main__":
    main()
