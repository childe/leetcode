#!/usr/bin/env python

"""
https://leetcode.cn/problems/search-a-2d-matrix-ii/description/

Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
 

Example 1:


Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true
Example 2:


Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= n, m <= 300
-10^9 <= matrix[i][j] <= 10^9
All the integers in each row are sorted in ascending order.
All the integers in each column are sorted in ascending order.
-10^9 <= target <= 10^9
"""


class Solution:
    def searchMatrix2(
        self,
        matrix: list[list[int]],
        target: int,
        start_row: int,
        end_row: int,
        start_col: int,
        end_col: int,
    ) -> bool:
        # print(start_row, end_row, start_col, end_col)
        # print([row[start_col : end_col + 1] for row in matrix[start_row : end_col + 1]])
        if start_col > end_col or start_row > end_row:
            return False

        m = (start_row + end_row) // 2, (start_col + end_col) // 2
        # print(f"m={m}")

        if m[0] == start_row and m[1] == start_col:
            for row in matrix[start_row : end_row + 2]:
                if target in row[start_col : end_col + 2]:
                    return True
            return False

        if matrix[m[0]][m[1]] == target:
            return True

        if matrix[m[0]][m[1]] > target:
            return (
                self.searchMatrix2(matrix, target, start_row, m[0], start_col, m[1])
                or self.searchMatrix2(
                    matrix, target, m[0], end_row, start_col, m[1] - 1
                )
                or self.searchMatrix2(
                    matrix, target, start_row, m[0] - 1, m[1], end_col
                )
            )

        return (
            self.searchMatrix2(matrix, target, m[0], end_row, m[1], end_col)
            or self.searchMatrix2(matrix, target, m[0] + 1, end_row, start_col, m[1])
            or self.searchMatrix2(matrix, target, start_row, m[0], m[1] + 1, end_col)
        )

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """
        >>> s=Solution()
        >>> s.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5)
        True
        >>> s.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20)
        False
        >>> s.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 1)
        True
        """
        return self.searchMatrix2(
            matrix, target, 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        )


s = Solution()
s.searchMatrix(
    [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ],
    20,
)
