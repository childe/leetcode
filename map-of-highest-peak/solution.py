#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/problems/map-of-highest-peak/

You are given an integer matrix isWater of size m x n that represents a map of land and water cells.

If isWater[i][j] == 0, cell (i, j) is a land cell.
If isWater[i][j] == 1, cell (i, j) is a water cell.
You must assign each cell a height in a way that follows these rules:

The height of each cell must be non-negative.
If the cell is a water cell, its height must be 0.
Any two adjacent cells must have an absolute height difference of at most 1. A cell is adjacent to another cell if the former is directly north, east, south, or west of the latter (i.e., their sides are touching).
Find an assignment of heights such that the maximum height in the matrix is maximized.

Return an integer matrix height of size m x n where height[i][j] is cell (i, j)'s height. If there are multiple solutions, return any of them.

Example 1:

Input: isWater = [[0,1],[0,0]]
Output: [[1,0],[2,1]]
Explanation: The image shows the assigned heights of each cell.
The blue cell is the water cell, and the green cells are the land cells.

Example 2:

Input: isWater = [[0,0,1],[1,0,0],[0,0,0]]
Output: [[1,1,0],[0,1,1],[1,2,2]]
Explanation: A height of 2 is the maximum possible height of any assignment.
Any height assignment that has a maximum height of 2 while still meeting the rules will also be accepted.

Constraints:

m == isWater.length
n == isWater[i].length
1 <= m, n <= 1000
isWater[i][j] is 0 or 1.
There is at least one water cell.
"""

from collections import deque


class Solution:
    def update_arround_cells(self, x, y, height, heights):
        updated = []
        for nx, ny in ((x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)):
            if (
                0 <= nx < self.width
                and 0 <= ny < self.height
                and heights[nx][ny] is None
            ):
                heights[nx][ny] = height + 1

                updated.append((nx, ny, height + 1))

        return updated

    def highestPeak(self, isWater: list[list[int]]) -> list[list[int]]:
        """
        >>> s= Solution()
        >>> s.highestPeak(isWater = [[0,1],[0,0]])
        [[1, 0], [2, 1]]
        >>> s.highestPeak(isWater = [[0,0,1],[1,0,0],[0,0,0]])
        [[1, 1, 0], [0, 1, 1], [1, 2, 2]]
        """

        self.height, self.width = len(isWater), len(isWater[0])

        heights = []
        for i, row in enumerate(isWater):
            heights.append([])
            for j, cell in enumerate(row):
                heights[i].append(None)

        self.this_level = []
        for i, row in enumerate(isWater):
            for j, cell in enumerate(row):
                if cell == 1:
                    self.this_level.insert(0, (i, j, 0))
                    heights[i][j] = 0

        # print(self.this_level)
        while self.this_level:
            x, y, height = self.this_level.pop()
            for n in self.update_arround_cells(x, y, height, heights):
                self.this_level.insert(0, n)

        return heights

    def highestPeak2(self, isWater: list[list[int]]) -> list[list[int]]:
        m, n = len(isWater), len(isWater[0])
        ans = [[water - 1 for water in row] for row in isWater]
        q = deque(
            (i, j)
            for i, row in enumerate(isWater)
            for j, water in enumerate(row)
            if water
        )  # 将所有水域入队
        while q:
            i, j = q.popleft()
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and ans[x][y] == -1:
                    ans[x][y] = ans[i][j] + 1
                    q.append((x, y))
        return ans


def main():
    s = Solution()
    isWater = []
    for _ in range(1024):
        isWater.append([0] * 1024)
    isWater[0][0] = 1
    s.highestPeak(isWater=isWater)


if __name__ == "__main__":
    main()
