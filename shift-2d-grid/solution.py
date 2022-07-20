#!/usr/bin/env python3


class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        """
        >>> s = Solution()
        >>> s.shiftGrid(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1)
        [[9, 1, 2], [3, 4, 5], [6, 7, 8]]
        >>> s.shiftGrid(grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4)
        [[12, 0, 21, 13], [3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10]]
        >>> s.shiftGrid(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9)
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        """
        if not grid:
            return grid
        m, n = len(grid), len(grid[0])
        total = m * n

        def position(x: int, y: int) -> int:
            return x * n + y

        def idx(position: int) -> tuple[int, int]:
            return (position // n, position % n)

        ans = []
        for i in range(m):
            row = [0] * n
            ans.append(row)
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                x, y = idx((position(i, j) + k) % total)
                ans[x][y] = v

        return ans
