# -*- coding: utf-8 -*-

'''
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
'''


class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        for i, row in enumerate(matrix):
            for j, c in enumerate(row):
                if c != 0:
                    row[j] = len(matrix) + len(row) + 1

        current = 0
        changed = True

        while changed:
            changed = False
            for i, row in enumerate(matrix):
                for j, c in enumerate(row):
                    if c != current:
                        continue

                    # up
                    if i > 0 and matrix[i-1][j] > current+1:
                        matrix[i-1][j] = current+1
                        changed = True

                    # down
                    if i < len(matrix)-1 and matrix[i+1][j] > current+1:
                        matrix[i+1][j] = current+1
                        changed = True

                    # left
                    if j > 0 and matrix[i][j-1] > current+1:
                        matrix[i][j-1] = current+1
                        changed = True

                    # right
                    if j < len(row)-1 and matrix[i][j+1] > current+1:
                        matrix[i][j+1] = current+1
                        changed = True


def main():
    s = Solution()

    matrix = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    output = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    s.updateMatrix(matrix)
    print(matrix)
    assert(output == matrix)

    matrix = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    output = [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
    s.updateMatrix(matrix)
    print(matrix)
    assert(output == matrix)


if __name__ == '__main__':
    main()
