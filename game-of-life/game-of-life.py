#!/usr/bin/env python3

"""
https://leetcode.cn/problems/game-of-life/description/
"""


class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                count = 0
                for x in range(max(0, i - 1), min(m, i + 2)):
                    for y in range(max(0, j - 1), min(n, j + 2)):
                        if x == i and y == j:
                            continue
                        if board[x][y] == 1 or board[x][y] == 2:
                            count += 1
                # print(i, j, count)
                if count < 2 or count > 3:
                    if board[i][j] == 1:
                        board[i][j] = 2  # 1 -> 0
                elif count == 3:
                    if board[i][j] == 0:
                        board[i][j] = 3  # 0 -> 1

        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == 3:
                    board[i][j] = 1


import unittest


class TestSolution(unittest.TestCase):
    def test_gameOfLife(self):
        self.solution = Solution()
        board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
        self.solution.gameOfLife(board)
        self.assertEqual(board, [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]])

        board = [[1, 1], [1, 0]]
        self.solution.gameOfLife(board)
        self.assertEqual(board, [[1, 1], [1, 1]])


if __name__ == "__main__":
    unittest.main()
