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

    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
                continue

            current = 0
            while stack:
                poped = stack.pop()
                if poped == '(':
                    if c == ')':
                        current += 2
                        c = None
                        continue
                    else:  # c is None
                        stack.append('(')
                        break
                elif poped == ')':
                    stack.append(poped)
                    break
                else:  # number
                    current += poped
                    continue

            if current != 0:
                stack.append(current)
            if c == ')':
                stack.append(')')

        max_length = 0
        for e in stack:
            if isinstance(e, int):
                max_length = max(max_length, e)

        return max_length


class TestSolution(unittest.TestCase):
    def test_longestValidParentheses(self):
        solution = Solution()

        s = ""
        rst = solution.longestValidParentheses(s)
        self.assertEqual(0, rst)

        s = "()"
        rst = solution.longestValidParentheses(s)
        self.assertEqual(2, rst)

        s = ")("
        rst = solution.longestValidParentheses(s)
        self.assertEqual(0, rst)

        s = ")()"
        rst = solution.longestValidParentheses(s)
        self.assertEqual(2, rst)

        s = "()()"
        rst = solution.longestValidParentheses(s)
        self.assertEqual(4, rst)

        s = "()()))())())))(()((()()()))())"
        rst = solution.longestValidParentheses(s)
        self.assertEqual(16, rst)

        s = "((())())(()))(()()(()(()))(()((((()))))))((()())()))()()(()(((((()()()())))()())(()()))((((((())))((()))()()))))(()))())))()))()())((()()))))(()(((((())))))()((()(()(())((((())(())((()()(()())))())(()(())()()))())(()()()))()(((()())(((()()())))(((()()()))(()()))()))()))))))())()()((()(())(()))()((()()()((())))()(((()())(()))())())))(((()))))())))()(())))()())))())()((()))((()))()))(((())((()()()(()((()((())))((()()))())(()()(()))))())((())))(()))()))))))()(()))())(()())))))(()))((())(()((())(((((()()()(()()())))(()())()((()(()()))(()(())((()((()))))))))(()(())()())()(()(()(()))()()()(()()())))(())(()((((()()))())))(())((()(())())))))())()()))(((())))())((()(()))(()()))((())(())))))(()(()((()((()()))))))(()()()(()()()(()(())()))()))(((()(())()())(()))())))(((()))())(()((()))(()((()()()(())()(()())()(())(()(()((((())()))(((()()(((()())(()()()(())()())())(()(()()((()))))()(()))))(((())))()()))(()))((()))))()()))))((((()(())()()()((()))((()))())())(()((()()())))))))()))(((()))))))(()())))(((()))((()))())))(((()(((())))())(()))))(((()(((((((((((((())(((()))((((())())()))())((((())(((())))())(((()))))()())()(())())(()))))()))()()()))(((((())()()((()))())(()))()()(()()))(())(()()))()))))(((())))))((()()(()()()()((())((((())())))))((((((()((()((())())(()((()))(()())())())(()(())(())(()((())((())))(())())))(()()())((((()))))((()(())(()(()())))))))))((()())()()))((()(((()((()))(((((()()()()()(()(()((()(()))(()(()((()()))))()(()()((((((()((()())()))((())()()(((((()(()))))()()((()())((()())()(())((()))()()(()))"
        rst = solution.longestValidParentheses(s)
        self.assertEqual(168, rst)


if __name__ == '__main__':
    unittest.main()
