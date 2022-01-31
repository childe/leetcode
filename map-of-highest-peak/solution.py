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
        for nx, ny in ((x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)):
            if (
                0 <= nx < self.width
                and 0 <= ny < self.height
                and heights[nx][ny] is None
            ):
                heights[nx][ny] = height + 1

                self.this_level.append((nx, ny, height + 1))

    def highestPeak(self, isWater: list[list[int]]) -> list[list[int]]:
        """
        >>> s= Solution()
        >>> s.highestPeak(isWater = [[0,1],[0,0]])
        [[1, 0], [2, 1]]
        >>> s.highestPeak(isWater = [[0,0,1],[1,0,0],[0,0,0]])
        [[1, 1, 0], [0, 1, 1], [1, 2, 2]]
        >>> s.highestPeak(isWater = [[0,0],[1,1],[1,0]])
        [[1, 1], [0, 0], [0, 1]]
        """
        h, w = len(isWater), len(isWater[0])
        # print(h, w)
        heights = [[0 if water else None for water in row] for row in isWater]
        # print(f"{heights=}")
        q = deque(
            (i, j, 0)
            for i, row in enumerate(isWater)
            for j, water in enumerate(row)
            if water
        )
        while q:
            # print(q)
            x, y, height = q.popleft()
            # print(x, y, height)
            for nx, ny in ((x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)):
                # print(f"{nx=} {ny=}")
                if 0 <= nx < h and 0 <= ny < w and heights[nx][ny] is None:
                    heights[nx][ny] = height + 1
                    q.append((nx, ny, height + 1))
            # print(heights)
        return heights


def main():
    s = Solution()
    isWater = []
    for _ in range(1024):
        isWater.append([0] * 1024)
    isWater[0][0] = 1
    s.highestPeak(isWater=isWater)
    # s.highestPeak(s.highestPeak(isWater=[[0, 0], [1, 1], [1, 0]]))


if __name__ == "__main__":
    main()
