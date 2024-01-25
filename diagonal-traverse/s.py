# -*- coding: utf-8 -*-

"""
https://leetcode.cn/problems/diagonal-traverse/
"""


class Solution:
    def next_pos(self, x, y, m, n, direction):
        if direction == 1:
            if x == m - 1:
                return (x, y + 1), -direction
            if y == 0:
                return (x + 1, y), -direction
            return (x + 1, y - 1), direction
        else:
            if y == n - 1:
                return (x + 1, y), -direction
            if x == 0:
                return (x, y + 1), -direction
            return (x - 1, y + 1), direction

    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        if not mat or not mat[0]:
            return []

        x, y = 0, 0
        direction = 1
        n, m = len(mat), len(mat[0])  # m 是宽，n 是高
        ans = []
        for _ in range(m * n):
            # print(x, y, direction)
            ans.append(mat[y][x])
            (x, y), direction = self.next_pos(x, y, m, n, direction)

        return ans


def main():
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(Solution().findDiagonalOrder(mat))
    mat = [[1, 2], [3, 4]]
    print(Solution().findDiagonalOrder(mat))
    mat = [[2, 3]]
    print(Solution().findDiagonalOrder(mat))


if __name__ == "__main__":
    main()
