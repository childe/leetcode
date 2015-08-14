#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/longest-palindromic-substring/
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.

动态规划
"""

import unittest


class Solution:

    def longestPalindrome(self, s):
        """
        # @param {string} s
        # @return {string}
        """
        if not s[1:]:
            return s

        t = {}
        for idx in range(len(s)):
            t.setdefault(idx, {idx:True})

        for idx, e in enumerate(s[1:]):
            idx += 1
            #print
            #print idx,e
            for i in xrange(idx-1):
                t[idx][i] = s[i] == s[idx] and t[idx-1][i+1]
            t[idx][idx-1] = s[idx] == s[idx-1]

            #for end, v in t.items():
                #for start, is_parlindrome in v.items():
                    #print start,end,s[start:end+1],is_parlindrome

        longest = (0, None, None)
        for end, v in t.items():
            for start, is_parlindrome in v.items():
                if is_parlindrome and end-start >= longest[0]:
                    longest = (end-start+1, start, end)

        return s[longest[1]:longest[2]+1]


class TestSolution(unittest.TestCase):

    def test_longestPalindrome(self):
        s = Solution()

        string = "aabbccbbaabbccbbaa"
        expect = string
        rst = s.longestPalindrome(string)
        self.assertEqual(rst,expect)

        string = "aaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaa"
        expect = "aaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaa"
        rst = s.longestPalindrome(string)
        self.assertEqual(rst,expect)

        for i in range(20):
            string = "c" * i
            rst = s.longestPalindrome(string)
            self.assertEqual(rst, string)

        rst = s.longestPalindrome("abcabcbb")
        self.assertEqual(rst, "bcb")

        rst = s.longestPalindrome("aaabaaaa")
        self.assertEqual(rst, "aaabaaa")

        string = "c" * 1000
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
