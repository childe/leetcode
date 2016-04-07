#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/valid-parentheses/

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""


class Solution(object):

    def isValid(self, s):
        '''
        :type s: str
        :rtype: bool
        >>> s = Solution()
        >>> s.isValid("()")
        True
        >>> s.isValid("([]{})")
        True
        >>> s.isValid("()[]{}")
        True
        >>> s.isValid('(]')
        False
        >>> s.isValid('([)]')
        False
        >>> s.isValid('])')
        False
        '''

        partners = {'{':'}', '[':']', '(':')' }
        rights = partners.values()

        stack = []
        for c in s:
            if stack and partners.get(stack[-1]) == c:
                stack.pop()
            elif c in rights:
                return False
            else:
                stack.append(c)

        return stack == []
