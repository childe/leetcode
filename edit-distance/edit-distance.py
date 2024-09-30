#!/usr/bin/env python3

"""
https://leetcode.cn/problems/edit-distance/
"""

from functools import lru_cache


class Solution:
    @lru_cache(None)
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)

        if word1[0] == word2[0]:
            return self.minDistance(word1[1:], word2[1:])

        change = 1 + self.minDistance(word1[1:], word2[1:])
        delete1 = 1 + self.minDistance(word1[1:], word2)
        delete2 = 1 + self.minDistance(word1, word2[1:])
        return min(change, delete1, delete2)


import unittest


class TestSolution(unittest.TestCase):
    def test_minDistance(self):
        solution = Solution()

        self.assertEqual(solution.minDistance("teacher", "tenace"), 3)
        self.assertEqual(
            solution.minDistance(
                "trinitrophenylmethylnitramine", "dinitrophenylhydrazine"
            ),
            10,
        )
        self.assertEqual(solution.minDistance("sea", "eat"), 2)
        self.assertEqual(solution.minDistance("horse", "ros"), 3)
        self.assertEqual(solution.minDistance("intention", "execution"), 5)
        self.assertEqual(
            solution.minDistance("dinitrophenylhydrazine", "acetylphenylhydrazine"), 6
        )


if __name__ == "__main__":
    unittest.main()
