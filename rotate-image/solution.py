# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/problems/rotate-image/

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]

"""


def p(matrix):
    for l in matrix:
        print(l)


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range((n + 1) // 2):
            start, end = i, n - 1 - i
            for j in range(start, end):
                tmp = matrix[i][j]
                y, x = i, j
                for _ in range(4):
                    ny, nx = x, n - 1 - y
                    matrix[ny][nx], tmp = tmp, matrix[ny][nx]
                    x, y = nx, ny


def main():
    s = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    a = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    s.rotate(matrix)
    p(matrix)
    assert a == matrix

    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]

    a = [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
    s.rotate(matrix)
    p(matrix)
    assert a == matrix

    matrix = [[1, 2], [3, 4]]
    a = [[3, 1], [4, 2]]
    s.rotate(matrix)
    p(matrix)
    assert a == matrix

    s.rotate([])
    s.rotate([1])


if __name__ == "__main__":
    main()
