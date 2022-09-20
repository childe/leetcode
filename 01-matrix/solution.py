# -*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/01-matrix/

Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

 

Example 1:

Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]
Example 2:

Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]
 

Note:

The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.
"""


class Solution(object):
    def updateMatrix(self, matrix: list[list[int]]) -> list[list[int]]:
        """
        >>> s= Solution()
        >>> s.updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
        [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        >>> s.updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]])
        [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
        >>> s.updateMatrix([[0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,1,0]])
        [[0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0]]
        """

        m, n = len(matrix), len(matrix[0])

        def valid(x: int, y: int) -> bool:
            return 0 <= x < m and 0 <= y < n

        batch = set()
        # next_batch = set()

        def visit(x: int, y: int):
            v = matrix[x][y]
            for nx, ny in ((x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)):
                if not valid(nx, ny):
                    continue

                if matrix[nx][ny] == 0:
                    continue

                if matrix[nx][ny] == 1:
                    matrix[nx][ny] = -(abs(v) + 1)
                    batch.add((nx, ny))
                else:
                    if abs(v) + 1 < abs(matrix[nx][ny]):
                        matrix[nx][ny] = -(abs(v) + 1)
                        batch.add((nx, ny))

        for x, row in enumerate(matrix):
            for y, v in enumerate(row):
                if v == 0:
                    batch.add((x, y))

        while batch:
            x, y = batch.pop()
            visit(x, y)

        for x, row in enumerate(matrix):
            for y, v in enumerate(row):
                row[y] = abs(v)

        return matrix
