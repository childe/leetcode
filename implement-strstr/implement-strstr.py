#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/implement-strstr/#/description

Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

'''


class Solution(object):

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        >>> s = Solution()
        >>> s.strStr('', '')
        0
        >>> s.strStr('abcd', '')
        0
        >>> s.strStr('', 'ab')
        -1
        >>> s.strStr('abcd', 'abcd')
        0
        >>> s.strStr('abcd', 'cd')
        2
        >>> s.strStr('abcd', 'bc')
        1
        >>> s.strStr('abcd', 'bce')
        -1
        >>> s.strStr('abcd', 'bcde')
        -1
        >>> s.strStr('abcd', 'dc')
        -1
        """
        for i, c in enumerate(haystack):
            if len(haystack)-len(needle) < i:
                return -1
            for j, cc in enumerate(needle):
                if cc != haystack[i+j]:
                    break
            else:
                return i
        return 0 if needle == '' else -1
