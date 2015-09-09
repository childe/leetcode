#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/valid-sudoku/

Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


A partially filled sudoku which is valid.
http://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells
need to be validated.
"""
import unittest


class Solution(object):

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in board:
            l = [None]*10
            for n in row:
                if n == ".":
                    continue
                if l[ord(n)-48] is not None:
                    return False
                l[ord(n)-48] = True

        for i in range(9):
            l = [None]*10
            for row in board:
                n = row[i]
                if n == ".":
                    continue
                if l[ord(n)-48] is not None:
                    return False
                l[ord(n)-48] = True

        for i in range(9):
            l = [None]*10
            for j in range(9):
                n = board[i/3*3+j/3][i % 3*3+j % 3]
                if n == ".":
                    continue
                if n == ".":
                    continue
                if l[ord(n)-48] is not None:
                    return False
                l[ord(n)-48] = True

        return True


class testSolution(unittest.TestCase):

    def test_isValidSudoku(self):
        s = Solution()

        board = []
        for i in range(9):
            row = []
            for j in range(9):
                row.append(".")
            board.append(row)
        self.assertTrue(s.isValidSudoku(board))

        board = []
        for i in range(9):
            row = []
            for j in range(9):
                row.append("1")
            board.append(row)
        self.assertFalse(s.isValidSudoku(board))

        board = [
        "53..7....",
        "6..195...",
        ".98....6.",
        "8...6...3",
        "4..8.3..1",
        "7...2...6",
        ".6....28.",
        "...419..5",
        "....8..79",]
        self.assertTrue(s.isValidSudoku(board))

        board = [
            ".6....5..",
            "1.7....6.",
            "....1...8",
            "..9.5....",
            "...4.....",
            ".........",
            ".......8.",
            "....25...",
            "5......97"]
        self.assertTrue(s.isValidSudoku(board))

if __name__ == '__main__':
    unittest.main()
