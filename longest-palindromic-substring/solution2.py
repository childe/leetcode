#!/usr/bin/env python
# -*- coding: utf-8 -*-

""""
https://leetcode.com/problems/longest-palindromic-substring/
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.

分治
"""

import unittest


class Solution:

    def _merge(self, s1, s2):
        """
        @param {string} s1,s2
        @return {string}
        """
        # print s1,s2
        n1 = len(s1)
        if n1 == 1:
            return "" if s1[0] != s2[0] else s1*2

        n2 = len(s2)
        if n2 == 1:
            return "" if s1[0] != s2[0] else s2*2

        i = 0
        while(i < n1 and i < n2 and s1[-i-1] == s2[i]):
            i += 1
        candidate = s1[-i:]+s2[:i] if i > 0 else ""

        ss1 = s1[:-1]
        i = 0
        while(i < n1-1 and i < n2 and ss1[-i-1] == s2[i]):
            i += 1
        candidate2 = s1[-i-1:]+s2[:i] if i > 0 else ""

        ss2 = s2[1:]
        i = 0
        while(i < n1 and i < n2-1 and s1[-i-1] == ss2[i]):
            i += 1
        candidate3 = s1[-i:]+s2[:i+1] if i > 0 else ""

        # print "candidate",candidate,candidate2,candidate3
        return sorted(
            [candidate, candidate2, candidate3], key=lambda e: len(e))[-1]

    def longestPalindrome(self, s):
        """
        @param {string} s
        @return {string}
        """
        # print "s",s
        if not s[1:]:
            return s
        if not s[2:]:
            return (s if s[0] == s[1] else s[0])

        left = self.longestPalindrome(s[:len(s)/2])
        # print "left",left
        right = self.longestPalindrome(s[len(s)/2:])
        # print "right",right
        merged = self._merge(s[:len(s)/2], s[len(s)/2:])
        # print "merged",merged
        return sorted(
            [left, right, merged], key=lambda e: len(e))[-1]


class TestSolution(unittest.TestCase):

    def test_longestPalindrome(self):
        s = Solution()

        #for i in range(20):
            #string = "c" * i
            #rst = s.longestPalindrome(string)
            #self.assertEqual(rst, string)

        rst = s.longestPalindrome("abcabcbb")
        self.assertEqual(rst, "bcb")

        rst = s.longestPalindrome("aaabaaaa")
        self.assertEqual(rst, "aaabaaa")

        string = "c" * 4000
        rst = s.longestPalindrome(string)
        self.assertEqual(rst, string)

        import random
        alphabet = [chr(e) for e in range(ord('a'), ord('z')+1)]
        for i in range(1000):
            string = ""
            for j in range(random.randint(1, 1000)):
                string += random.choice(alphabet)
            self.assertTrue(s.longestPalindrome(string) in string)


if __name__ == '__main__':
    unittest.main()
