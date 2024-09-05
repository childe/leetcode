#!/usr/bin/env python3
"""
https://leetcode.cn/problems/surrounded-regions/description/
"""


class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        w, h = len(board[0]), len(board)

        def dfs_fill_edge_cell(x: int, y: int):
            if x < 0 or x >= w or y < 0 or y >= h:
                return

            if board[y][x] == "O":
                board[y][x] = "edge"
                for offset_x, offset_y in ((0, -1), (-1, 0), (1, 0), (0, 1)):
                    dfs_fill_edge_cell(x + offset_x, y + offset_y)

        for y in range(h):
            for x in range(w):
                if (x == 0 or x == w - 1 or y == 0 or y == h - 1) and board[y][
                    x
                ] == "O":
                    dfs_fill_edge_cell(x, y)

        for row in board:
            for x, c in enumerate(row):
                if c == "edge":
                    row[x] = "O"
                if c == "O":
                    row[x] = "X"


import unittest


class TestSolution(unittest.TestCase):

    def test_solve(self):
        s = Solution()
        board = [
            ["O", "O", "O", "O", "O"],
            ["O", "X", "X", "X", "O"],
            ["O", "X", "X", "X", "O"],
            ["O", "X", "X", "X", "O"],
            ["O", "O", "O", "O", "O"],
        ]
        s.solve(board)
        self.assertEqual(
            [
                ["O", "O", "O", "O", "O"],
                ["O", "X", "X", "X", "O"],
                ["O", "X", "X", "X", "O"],
                ["O", "X", "X", "X", "O"],
                ["O", "O", "O", "O", "O"],
            ],
            board,
        )

        board = [
            ["O", "X", "X", "O", "X"],
            ["X", "O", "O", "X", "O"],
            ["X", "O", "X", "O", "X"],
            ["O", "X", "O", "O", "O"],
            ["X", "X", "O", "X", "O"],
        ]
        s.solve(board)
        self.assertEqual(
            [
                ["O", "X", "X", "O", "X"],
                ["X", "X", "X", "X", "O"],
                ["X", "X", "X", "O", "X"],
                ["O", "X", "O", "O", "O"],
                ["X", "X", "O", "X", "O"],
            ],
            board,
        )

        board = [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"],
        ]
        s.solve(board)
        self.assertEqual(
            [
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "O", "X", "X"],
            ],
            board,
        )


if __name__ == "__main__":
    unittest.main()
