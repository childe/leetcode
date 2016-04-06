#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

'''
https://leetcode.com/problems/generate-parentheses/

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
'''


class Solution(object):

    def _add_one_to_element(self, element):
        """
        :type element: tuple or int
        :rtype: tuple or int
        """
        if isinstance(element, int):
            return element+1
        elif isinstance(element, tuple):
            return (element,)
        else:
            raise Exception("element must be int or tuple")

    def _add_one_to_parentheses(self, parentheses):
        """
        :type parentheses: tuple[int]
        :rtype: tuple

        >>> s = Solution()

        >>> parentheses = (1,)
        >>> sorted(s._add_one_to_parentheses(parentheses))
        [(1, 1), (2,)]

        >>> parentheses = (1,1)
        >>> sorted(s._add_one_to_parentheses(parentheses))
        [(1, 1, 1), (1, 2), (2, 1), ((1, 1),)]

        >>> parentheses = ((1,1),)
        >>> sorted(s._add_one_to_parentheses(parentheses))
        [(1, (1, 1)), ((1, 1), 1), (((1, 1),),)]
        """
        rst = set()
        for i in range(1+len(parentheses)):
            rst.add((parentheses[:i] + (1, ) + parentheses[i:]))
            # print 1, rst

        for i, e in enumerate(parentheses):
            rst.add(
                (parentheses[: i] + (self._add_one_to_element(e),) +
                 parentheses[i + 1:]))
            # print 2, rst

        if len(parentheses) > 1:
            rst.add((parentheses,))
        # print 3, rst

        return tuple(rst)

    def _generateParenthesis(self, n):
        """
        :type n: int
        :rtype: tuple

        >>> s = Solution()

        >>> sorted(s._generateParenthesis(1))
        [(1,)]

        >>> sorted(s._generateParenthesis(2))
        [(1, 1), (2,)]

        >>> sorted(s._generateParenthesis(3))
        [(1, 1, 1), (1, 2), (2, 1), (3,), ((1, 1),)]
        """

        rst = ((1,),)
        for i in range(2, n+1):
            _temp = tuple()
            for parentheses in rst:
                _temp += self._add_one_to_parentheses(parentheses)
            rst = tuple(set(_temp))
        return rst

    def _render_parentheses(self, parentheses):
        """
        :type parentheses: tuple
        :rtype: string
        >>> s = Solution()

        >>> s._render_parentheses((1,))
        '(())'

        >>> s._render_parentheses((1,1))
        '(()())'

        >>> s._render_parentheses(((1,1),))
        '((()()))'

        >>> s._render_parentheses((1,2))
        '(()(()))'

        """
        if isinstance(parentheses, int):
            return '('*parentheses + ')'*parentheses
        elif isinstance(parentheses, tuple):
            return '(%s)' % ''.join(self._render_parentheses(p)
                                    for p in parentheses)
        else:
            raise Exception("element must be int or tuple")

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: list[str]
        >>> s = Solution()

        >>> s.generateParenthesis(1)
        ['()']

        >>> s.generateParenthesis(2)
        ['(())', '()()']

        >>> s.generateParenthesis(3)
        ['()(())', '()()()', '((()))', '(()())', '(())()']
        """
        parenthesis = self._generateParenthesis(n)
        rst = []
        for p in parenthesis:
            rst.append(self._render_parentheses(p)[1:-1])

        return rst
