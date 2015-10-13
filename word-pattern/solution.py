#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/word-pattern/

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.

Credits:
Special thanks to @minglotus6 for adding this problem and creating all test cases.

Show Tags
Show Similar Problems
"""
import unittest


class Solution(object):

    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split(" ")

        if len(pattern) != len(words):
            return False

        mapping = {}
        for idx, c in enumerate(pattern):
            if c not in mapping:
                if words[idx] in mapping.values():
                    return False
                mapping[c] = words[idx]
                continue
            if mapping[c] != words[idx]:
                return False
        return True


class TestSolution(unittest.TestCase):

    def test_wordPattern(self):
        s = Solution()
        pattern = "abba"
        str = "dog cat cat dog"
        self.assertTrue(s.wordPattern(pattern, str))

        pattern = "abba"
        str = "dog cat cat fish"
        self.assertFalse(s.wordPattern(pattern, str))

        pattern = "aaaa"
        str = "dog cat cat dog"
        self.assertFalse(s.wordPattern(pattern, str))

        pattern = "abba"
        str = "dog dog dog dog"
        self.assertFalse(s.wordPattern(pattern, str))

        pattern = "abb"
        str = "dog dog dog dog"
        self.assertFalse(s.wordPattern(pattern, str))

if __name__ == '__main__':
    unittest.main()
