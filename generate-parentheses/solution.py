#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/generate-parentheses/

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
'''


class Solution(object):

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

        cache = {0:set(),1:{"()"}}

        def abcd(n):
            if n in cache:
                return cache[n]
            else:
                rst = set()
                for i in range(1,n):
                    rst_a = abcd(i)
                    rst_b = abcd(n-i)
                    rst.update({a+b for a in rst_a for b in rst_b})
                rst.update({'(%s)'%e for e in abcd(n-1)})
                cache[n] = rst
                return rst

        return list(abcd(n))
