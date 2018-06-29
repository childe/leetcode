#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/decode-ways/description/

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:
Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
'''


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        >>> s = Solution()
        >>> s.numDecodings('12')
        2
        >>> s.numDecodings('226')
        3
        >>> s.numDecodings('2222')
        5
        >>> s.numDecodings('0')
        0
        >>> s.numDecodings('2002')
        0
        >>> s.numDecodings('2022')
        2
        >>> s.numDecodings('10')
        1
        >>> s.numDecodings('230')
        0
        >>> s.numDecodings('2685')
        2
        """
        if s == '':
            return 0
        if s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        if len(s) == 2:
            if s[1] == '0':
                return 0 if s[0] > '2' else 1
            return 2 if int(s) <= 26 else 1
        if int(s[:2]) <= 26:
            return self.numDecodings(s[1:]) + self.numDecodings(s[2:])
        return self.numDecodings(s[1:])

if __name__ == '__main__':
    import sys
    s = Solution()
    print s.numDecodings(sys.argv[1])
