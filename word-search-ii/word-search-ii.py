#!/usr/bin/env python3

"""
https://leetcode.cn/problems/word-search-ii/
"""


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        all_chars = set([c for row in board for c in row])
        words = [word for word in words if not (set(word) - all_chars)]

        all_chars_in_words = set([c for word in words for c in word])
        for row in board:
            for i, c in enumerate(row):
                if c not in all_chars_in_words:
                    row[i] = "#"

        ans = set()

        def dfs(
            board: list[list[str]], i: int, j: int, words_idx: list[int], char_idx: int
        ):
            c = board[i][j]
            next_words_idx = [
                idx
                for idx in words_idx
                if words[idx][char_idx:] and words[idx][char_idx] == c
            ]
            if not next_words_idx:
                return
            ans.update(
                [
                    words[idx]
                    for idx in next_words_idx
                    if len(words[idx]) == char_idx + 1
                ]
            )
            next_words_idx = [
                idx for idx in next_words_idx if len(words[idx]) > char_idx + 1
            ]

            for d in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                x, y = i + d[0], j + d[1]
                if (
                    0 <= x < len(board)
                    and 0 <= y < len(board[0])
                    and board[x][y] != "#"
                ):
                    board[i][j] = "#"
                    dfs(board, x, y, next_words_idx, char_idx + 1)
                    board[i][j] = c

        # dfs(board, 1, 3, list(range(len(words))), 0)
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(board, i, j, list(range(len(words))), 0)
        return sorted(list(ans))


import unittest


class TestSolution(unittest.TestCase):
    def test_findWords(self):
        solution = Solution()
        self.assertEqual(
            solution.findWords([["a", "b"], ["d", "c"]], ["abcd"]), ["abcd"]
        )
        self.assertEqual(
            solution.findWords(
                [
                    ["o", "a", "a", "n"],
                    ["e", "t", "a", "e"],
                    ["i", "h", "k", "r"],
                    ["i", "f", "l", "v"],
                ],
                ["oath", "pea", "eat", "rain"],
            ),
            [
                "eat",
                "oath",
            ],
        )
        self.assertEqual(solution.findWords([["a", "b"], ["c", "d"]], ["abcb"]), [])

        board = [
            ["m", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"],
            ["n", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
            ["o", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
            ["p", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
            ["q", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
            ["r", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
            ["s", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
            ["t", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
            ["u", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
            ["v", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
            ["w", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
            ["x", "y", "z", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
        ]
        words = [
            "aaaaaaaaaa",
            "aaaaaaaaab",
            "aaaaaaaabc",
        ]

        print(solution.findWords(board, words))


if __name__ == "__main__":
    unittest.main()
