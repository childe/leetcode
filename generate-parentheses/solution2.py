#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/generate-parentheses/

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
"""


class Solution(object):
    def __init__(self):
        self.cache = {}

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: list[str]
        >>> s = Solution()
        >>> s.generateParenthesis(1)
        ['()']
        >>> s.generateParenthesis(2)
        ['()()', '(())']
        >>> s.generateParenthesis(3)
        ['()(())', '((()))', '(()())', '(())()', '()()()']
        >>> len(s.generateParenthesis(6))
        132
        >>> len(s.generateParenthesis(7))
        429
        """
        if n == 0:
            return set([""])

        # if n == 1:
        # return set(["()"])

        if n in self.cache:
            return self.cache[n]

        rst = set()
        for i in range(n):
            for left_part in self.generateParenthesis(n - i - 1):
                for right_part in self.generateParenthesis(i):
                    rst.add("(%s)%s" % (left_part, right_part))

        self.cache[n] = rst
        return list(rst)
