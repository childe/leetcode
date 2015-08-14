#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/longest-palindromic-substring/
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.

动态规划??
"""

import unittest


class Solution:

    def _is_palindrome(self, first_c, palindrome, last_c):
        # print first_c, palindrome, last_c
        if palindrome[2] and palindrome[0][0] == last_c:
            return (palindrome[0]+last_c, palindrome[1]+1, True)

        if first_c == last_c:
            return (first_c+palindrome[0]+last_c, palindrome[1]+2, False)

        return False

    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        if not s:
            return
        longest = ("", 0, False)
        palindromes_endswith_last_c = {}
        for idx, e in enumerate(s):
            # print
            # print idx,e
            if longest[1] <= 1:
                longest = (e, 1, True)

            new_set = {(e, 1, True)}
            longest_in_new_set = False
            for palindrome in palindromes_endswith_last_c:
                pre_c = s[idx-palindrome[1]-1] if idx > palindrome[1] else None
                # print "pre_c",pre_c
                n = self._is_palindrome(pre_c, palindrome, e)

                # print "n",n
                if n is not False:
                    new_set.add(n)

                    if n[1] >= longest[1]:
                        longest = n
                        longest_in_new_set = True

            palindromes_endswith_last_c = new_set
            # print new_set, longest
            if longest_in_new_set and longest[2]:
                palindromes_endswith_last_c = {longest}
            # print palindromes_endswith_last_c, longest

        return longest[0]


class TestSolution(unittest.TestCase):

    def test_longestPalindrome(self):
        s = Solution()
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
