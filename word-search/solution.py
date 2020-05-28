# -*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/word-search/

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
 

Constraints:

board and word consists only of lowercase and uppercase English letters.
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3
"""


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        new_board = [['']+row+[''] for row in board]
        new_board.insert(0, ['']*(2+len(board[0])))
        new_board.append(['']*(2+len(board[0])))
        board = new_board

        candidates = []
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c == word[0]:
                    candidates.append((i, j))

        print(candidates)
        for i, j in candidates:
            print(i, j)
            if self.p(i, j, board, word):
                return True
        return False

    def p(self, i, j, board, word):
        directions = ((-1, 0), (0, 1), (1, 0), (0, -1))

        step, dir_idx, original_char = 1, 0, board[i][j]
        stack = [[i, j, step, original_char, dir_idx]]
        board[i][j] = ''
        while stack:
            print(len(stack))
            print(stack[-1])
            i, j, step, original_char, dir_idx = stack[-1]
            if step == len(word):
                return True
            # 需要回溯
            if dir_idx == len(directions):
                board[i][j] = original_char
                stack.pop()
                continue
            stack[-1][-1] += 1
            x, y = directions[dir_idx]
            if board[i+x][j+y] == word[step]:
                board[i+x][j+y] = ''
                stack.append([i+x, j+y, step+1, word[step], 0])

        return False


def main():
    s = Solution()

    board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
    ]
    assert s.exist(board, "ABCCED") is True
    assert s.exist(board, "SEE") is True
    assert s.exist(board, "ABCB") is False

    board = [
        ['A', 'A'],
    ]
    assert s.exist(board, "AAA") is False


if __name__ == '__main__':
    main()
