#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


class Solution:
    # @param {string} s
    # @return {integer}

    def lengthOfLongestSubstring(self, s):
        current_length = 0
        current_str = ""
        longestLength = 0
        for e in s:
            if e not in current_str:
                current_str += e
                current_length += 1
                if current_length >= longestLength:
                    longestLength = current_length
            else:
                current_str = current_str[current_str.index(e)+1:] + e
                current_length = len(current_str)

        return longestLength


class TestSolution(unittest.TestCase):

    def test_addTwoNumbers(self):
        s = Solution()
        rst = s.lengthOfLongestSubstring("abcabcbb")
        self.assertEqual(rst, 3)

        rst = s.lengthOfLongestSubstring("bbbbb")
        self.assertEqual(rst, 1)


if __name__ == '__main__':
    unittest.main()
