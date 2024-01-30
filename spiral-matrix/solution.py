# -*- coding: utf-8 -*-
"""
https://leetcode.cn/problems/spiral-matrix/description/

给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。


m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""


class Solution:
    def position_valid(self, h, w, m, n, round_idx, dir_idx) -> bool:
        if m == n == round_idx:
            if dir_idx == 0:
                return True
            return False

        if m < round_idx or m >= h - round_idx:
            return False
        if n < round_idx or n >= w - round_idx:
            return False

        return True

    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        h, w = len(matrix), len(matrix[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_idx = 0
        m, n = 0, -1
        round_idx = 0
        ans = []
        while len(ans) < h * w:
            nm, nn = m + directions[dir_idx][0], n + directions[dir_idx][1]
            if self.position_valid(h, w, nm, nn, round_idx, dir_idx):
                m, n = nm, nn
                ans.append(matrix[m][n])
            else:
                dir_idx = (dir_idx + 1) % 4
                if dir_idx == 0:
                    round_idx += 1

        return ans


def main():
    s = Solution()
    print(s.spiralOrder(matrix=[[]]))
    print(s.spiralOrder(matrix=[[1]]))
    print(s.spiralOrder(matrix=[[1, 2, 3]]))
    print(s.spiralOrder(matrix=[[1, 2, 3]]))
    print(s.spiralOrder(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(s.spiralOrder(matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))


if __name__ == "__main__":
    main()
