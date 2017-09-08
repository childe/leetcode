#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/sudoku-solver/description/

Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.
"""


class Solution(object):
    BIGSTEPS = 9
    SMALLSTEPS = 3

    def _createTestBorad(self):
        """
        :type List[List[str]]
        """
        board = []
        board.append(list('53..7....'))
        board.append(list('6..195...'))
        board.append(list('.98....6.'))
        board.append(list('8...6...3'))
        board.append(list('4..8.3..1'))
        board.append(list('7...2...6'))
        board.append(list('.6....28.'))
        board.append(list('...419..5'))
        board.append(list('....8..79'))
        return board

    def findAllValidChars(self, board, row, col):
        """
        :type board: List[List[str]]
        :type row: int
        :type cloe: int
        :rtype: []char

        >>> s = Solution()
        >>> board = s._createTestBorad()
        >>> s.findAllValidChars(board, 0, 2)
        ['1', '2', '4']
        >>> s.findAllValidChars(board, 2, 4)
        ['3', '4']
        """
        rst = []
        for e in range(1, Solution.BIGSTEPS+1):
            if str(e) in [c[-1] for c in board[row]]:
                continue
            if str(e) in [rowChars[col][-1] for rowChars in board]:
                continue
            for rowChars in board[row /
                                  Solution.SMALLSTEPS *
                                  Solution.SMALLSTEPS: row /
                                  Solution.SMALLSTEPS *
                                  Solution.SMALLSTEPS +
                                  Solution.SMALLSTEPS]:
                if str(e) in[c[-1]
                             for c in rowChars
                             [col / Solution.SMALLSTEPS * Solution.SMALLSTEPS: col / Solution.SMALLSTEPS *
                              Solution.SMALLSTEPS + Solution.SMALLSTEPS]]:
                    break
            else:
                rst.append(str(e))

        return rst

    def findNextValidChar(self, board, row, col):
        """
        :type board: List[List[str]]
        :type row: int
        :type cloe: int
        :rtype: char

        >>> s = Solution()
        >>> board = s._createTestBorad()
        >>> s.findNextValidChar(board, 0, 2)
        '1'
        >>> s.findNextValidChar(board, 1, 1)
        '2'
        >>> s.findNextValidChar(board, 3, 7)
        '2'
        """
        c = board[row][col][-1]
        c = 0 if c == '.' else int(c)
        # print 'c', c
        for e in range(c+1, Solution.BIGSTEPS+1):
            # print 'e', e
            if str(e) in [c[-1] for c in board[row]]:
                continue
            if str(e) in [rowChars[col][-1] for rowChars in board]:
                continue
            for rowChars in board[row /
                                  Solution.SMALLSTEPS *
                                  Solution.SMALLSTEPS: row /
                                  Solution.SMALLSTEPS *
                                  Solution.SMALLSTEPS +
                                  Solution.SMALLSTEPS]:
                if str(e) in[c[-1]
                             for c in rowChars
                             [col / Solution.SMALLSTEPS * Solution.SMALLSTEPS: col / Solution.SMALLSTEPS *
                              Solution.SMALLSTEPS + Solution.SMALLSTEPS]]:
                    break
            else:
                return str(e)

        return None

    def rollBack(self, board, row, col):
        """
        skip originally existed char

        :rtype: (int,int)

        >>> s = Solution()
        >>> board = s._createTestBorad()
        >>> s.rollBack(board, 8, 8)
        (8, 6)
        >>> s.rollBack(board, 1, 3)
        (1, 2)
        >>> s.rollBack(board, 5, 1)
        (4, 7)
        >>> s.rollBack(board, 0, 2)
        """
        board[row][col] = '.'
        while row >= 0:
            rowChars = board[row]
            for i in range(col-1, -1, -1):
                c = rowChars[i]
                if c.startswith('.'):
                    return row, i
            row -= 1
            col = len(board[row])
        return None

    def findNextCell(self, board, row, col):
        """
        skip originally existed char

        :rtype: (int,int)
        >>> s = Solution()
        >>> board = s._createTestBorad()
        >>> s.findNextCell(board, 0, -1)
        (0, 2)
        >>> s.findNextCell(board, 1, 0)
        (1, 1)
        >>> s.findNextCell(board, 1, 3)
        (1, 6)
        >>> s.findNextCell(board, 3, 8)
        (4, 1)
        >>> s.findNextCell(board, 5, 7)
        (6, 0)
        >>> s.findNextCell(board, 8, 6)
        """
        while row < len(board):
            rowChars = board[row]
            for i in range(col+1, len(rowChars)):
                c = rowChars[i]
                if c.startswith('.'):
                    return row, i
            row, col = row+1, -1
        return None

    def removeDot(self, board):
        for row in board:
            for j, _ in enumerate(row):
                row[j] = row[j][-1]

    def solveSudoku(self, board):
        """
        : type board: List[List[str]]
        : rtype: void Do not return anything, modify board in-place instead.
        """
        cell = [0, -1]  # start
        isRollBack = False
        while True:
            # print '~' * 10
            # print 'isRollBack', isRollBack
            # print 'cell now', cell
            # for row in board:
                # print '\t'.join(row)

            if isRollBack is False:
                cell = self.findNextCell(board, *cell)
            # print 'processing cell', cell

            if cell is None:  # done
                # print 'done'
                self.removeDot(board)
                return

            nextValidChar = self.findNextValidChar(board, *cell)
            if nextValidChar is None:
                cell = self.rollBack(board, *cell)
                if cell is None:
                    # print 'failed'
                    return  # fail
                isRollBack = True
                # print 'will rollback'
            else:
                # print 'try', nextValidChar
                board[cell[0]][cell[1]] = '.' + nextValidChar
                isRollBack = False

            # for row in board:
                # print '\t'.join(row)


if __name__ == '__main__':
    s = Solution()
    board = s._createTestBorad()
    for row in board:
        print '\t'.join(row)
    s.solveSudoku(board)
    for row in board:
        print '\t'.join(row)
