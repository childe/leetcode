# -*- coding: utf-8 -*-

'''
https://leetcode-cn.com/problems/set-matrix-zeroes/

给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。

示例 1:

输入:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
示例 2:

输入:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
输出:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
进阶:

一个直接的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
你能想出一个常数空间的解决方案吗？


第一想法是遇到0就Set它所在的行和列.
但是被 Set 的格子会影响它后面或者下面的值,
所以要想办法处理这个问题,
一个方法是不要设置为0, 而是先设置为 None
'''


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                if cell != 0:
                    continue
                for l in range(0, len(row)):
                    if row[l] != 0:
                        row[l] = None
                for l in range(0, len(matrix)):
                    if matrix[l][j] != 0:
                        matrix[l][j] = None

        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                if row[j] is None:
                    row[j] = 0

def main():
    s = Solution()
    input = [[0, 1, 2, 0],
             [3, 4, 5, 2],
             [1, 3, 1, 5]
             ]
    output = [[0, 0, 0, 0],
              [0, 4, 5, 0],
              [0, 3, 1, 0]
              ]
    s.setZeroes(input)
    print(input)
    assert(input == output)


if __name__ == '__main__':
    main()
