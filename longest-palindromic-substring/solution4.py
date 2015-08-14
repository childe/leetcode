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
            t.setdefault(idx, {idx: (1, True)})
        if s[0] == s[1]:
            t[1][0] = (2, True)
            t[1].pop(1)

        for idx, e in enumerate(s[2:]):
            print
            print idx, e
            idx += 2
            for start, (length, is_successive) in t[idx-1].items():
                if start-1>=0 and s[start-1] == e:
                    if is_successive and s[start] == e:
                        t[idx][start-1] = (length+2, True)
                        t[idx].pop(idx)
                    else:
                        t[idx][start-1] = (length+2, False)
                elif is_successive and s[start] == e:
                    t[idx][start] = (length+1, True)
                    t[idx].pop(idx)

            for end, v in t.items():
                for start, (length, is_successive) in v.items():
                    print start, end, s[start:end+1], is_successive

        longest = (0, None, None)
        for end, v in t.items():
            for start, (length, is_successive) in v.items():
                if length > longest[0]:
                    longest = (length, start, end)

        return s[longest[1]:longest[2]+1]


class TestSolution(unittest.TestCase):

    def test_longestPalindrome(self):
        s = Solution()

        string = "aabbccbbaabbccbbaa"
        expect = string
        rst = s.longestPalindrome(string)
        self.assertEqual(rst,expect)
        return

        for i in range(0,10):
            string = "c" * i
            rst = s.longestPalindrome(string)
            self.assertEqual(rst, string)


        string = "aaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaa"
        expect = "aaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaa"
        rst = s.longestPalindrome(string)
        self.assertEqual(rst, expect)

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
