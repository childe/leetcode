#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

"""
https://leetcode.com/problems/longest-valid-parentheses/description/

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
"""


class Solution(object):
    def _isValid(self, intermediate, s, start, startChar, end, endChar):
        # print start, startChar, end, endChar
        # if startChar == ')' or endChar == '(':
            # return False

        # ()
        if end-start == 1:
            return True

        # (XX)
        if intermediate[start+1] and intermediate[start+1][-1] == end-1:
            return True

        # (X)(X)
        for i in intermediate[start]:
            if intermediate[i+1] and intermediate[i+1][-1] == end:
                return True

        return False

    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0

        intermediate = {}

        # init
        for i in range(len(s)):
            intermediate[i] = []

        # N
        for end, endChar in enumerate(s):
            if endChar == '(':
                continue
            for start in range(end-1, -1, -1):
                if s[start] == ')':
                    continue
                if self._isValid(
                        intermediate,
                        s,
                        start,
                        s[start],
                        end,
                        endChar):
                    intermediate[start].append(end)

        # find the result
        max_length = 0
        for start, ends in intermediate.items():
            if ends:
                max_length = max(1+ends[-1]-start, max_length)

        return max_length


class TestSolution(unittest.TestCase):
    def test_longestValidParentheses(self):
        solution = Solution()

        # s = ""
        # rst = solution.longestValidParentheses(s)
        # self.assertEqual(0, rst)

        # s = "()"
        # rst = solution.longestValidParentheses(s)
        # self.assertEqual(2, rst)

        # s = ")("
        # rst = solution.longestValidParentheses(s)
        # self.assertEqual(0, rst)

        # s = ")()"
        # rst = solution.longestValidParentheses(s)
        # self.assertEqual(2, rst)

        # s = "()()"
        # rst = solution.longestValidParentheses(s)
        # self.assertEqual(4, rst)

        s = "()()))())())))(()((()()()))())"
        rst = solution.longestValidParentheses(s)
        self.assertEqual(16, rst)

        s = "((())())(()))(()()(()(()))(()((((()))))))((()())()))()()(()(((((()()()())))()())(()()))((((((())))((()))()()))))(()))())))()))()())((()()))))(()(((((())))))()((()(()(())((((())(())((()()(()())))())(()(())()()))())(()()()))()(((()())(((()()())))(((()()()))(()()))()))()))))))())()()((()(())(()))()((()()()((())))()(((()())(()))())())))(((()))))())))()(())))()())))())()((()))((()))()))(((())((()()()(()((()((())))((()()))())(()()(()))))())((())))(()))()))))))()(()))())(()())))))(()))((())(()((())(((((()()()(()()())))(()())()((()(()()))(()(())((()((()))))))))(()(())()())()(()(()(()))()()()(()()())))(())(()((((()()))())))(())((()(())())))))())()()))(((())))())((()(()))(()()))((())(())))))(()(()((()((()()))))))(()()()(()()()(()(())()))()))(((()(())()())(()))())))(((()))())(()((()))(()((()()()(())()(()())()(())(()(()((((())()))(((()()(((()())(()()()(())()())())(()(()()((()))))()(()))))(((())))()()))(()))((()))))()()))))((((()(())()()()((()))((()))())())(()((()()())))))))()))(((()))))))(()())))(((()))((()))())))(((()(((())))())(()))))(((()(((((((((((((())(((()))((((())())()))())((((())(((())))())(((()))))()())()(())())(()))))()))()()()))(((((())()()((()))())(()))()()(()()))(())(()()))()))))(((())))))((()()(()()()()((())((((())())))))((((((()((()((())())(()((()))(()())())())(()(())(())(()((())((())))(())())))(()()())((((()))))((()(())(()(()())))))))))((()())()()))((()(((()((()))(((((()()()()()(()(()((()(()))(()(()((()()))))()(()()((((((()((()())()))((())()()(((((()(()))))()()((()())((()())()(())((()))()()(()))"
        rst = solution.longestValidParentheses(s)
        self.assertEqual(168, rst)


if __name__ == '__main__':
    unittest.main()
