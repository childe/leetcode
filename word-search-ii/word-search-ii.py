#!/usr/bin/env python3

"""
https://leetcode.cn/problems/word-search-ii/
"""

from collections import defaultdict


class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.word = ""  # 用于存储完整单词，默认为空

    def insert(self, word):
        cur = self
        for c in word:
            cur = cur.children[c]
        cur.word = word  # 在末尾节点存储完整的单词


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        all_chars = set([c for row in board for c in row])
        words = [word for word in words if not (set(word) - all_chars)]

        all_chars_in_words = set([c for word in words for c in word])
        for row in board:
            for i, c in enumerate(row):
                if c not in all_chars_in_words:
                    row[i] = "#"

        root = Trie()
        for word in words:
            root.insert(word)

        ans = set()

        def dfs(ti: Trie, i: int, j: int):
            c = board[i][j]
            if c == "#" or c not in ti.children:
                return
            if ti.children[c].word:
                ans.add(ti.children[c].word)
                ti.children[c].word = ""  # 防止重复添加
            for d in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                x, y = i + d[0], j + d[1]
                if 0 <= x < len(board) and 0 <= y < len(board[0]):
                    board[i][j] = "#"
                    dfs(ti.children[c], x, y)
                    board[i][j] = c

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(root, i, j)
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
