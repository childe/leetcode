#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst
an array of strings.
"""

import unittest


class Solution(object):

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        while(len(strs) > 1):
            s1 = strs.pop()
            s2 = strs.pop()
            if s1 == "" or s2 == "":
                return ""
            for i in range(min(len(s1), len(s2))):
                if s1[i] != s2[i]:
                    break
            else:
                i+=1
            if i == 0:
                return ""
            strs.insert(0, s1[:i])

        return strs[0]


class TestSolution(unittest.TestCase):

    def test_longestCommonPrefix(self):
        s = Solution()

        strs = ["aa","ab"]
        rst = s.longestCommonPrefix(strs)
        self.assertEqual("a",rst)

        strs = ["c","c"]
        rst = s.longestCommonPrefix(strs)
        self.assertEqual("c",rst)

        import random
        candidates = "abc"
        strs = []
        for i in range(10):
            strs.append("abcd" +
                        ''.join(
                            [random.choice(candidates)
                             for i in range(random.randint(0, 100))]))
        rst = s.longestCommonPrefix(strs)

        for e in strs:
            self.assertTrue(e.startswith(rst))


if __name__ == '__main__':
    unittest.main()
