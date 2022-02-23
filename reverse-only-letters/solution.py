#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/problems/reverse-only-letters/

917. Reverse Only Letters
Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.

Example 1:

Input: s = "ab-cd"
Output: "dc-ba"
Example 2:

Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
 

Constraints:

1 <= s.length <= 100
s consists of characters with ASCII values in the range [33, 122].
s does not contain '\"' or '\\'.
通过次数52,770提交次数88,080
"""


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        """
        >>> s = Solution()
        >>> s.reverseOnlyLetters("ab-cd")
        'dc-ba'
        >>> s.reverseOnlyLetters("a-bC-dEf-ghIj")
        'j-Ih-gfE-dCba'
        >>> s.reverseOnlyLetters("ab")
        'ba'
        >>> s.reverseOnlyLetters("abc")
        'cba'
        >>> s.reverseOnlyLetters("a-bc")
        'c-ba'
        >>> s.reverseOnlyLetters("7_28]")
        '7_28]'
        """
        i, j = 0, len(s) - 1
        ss = list(s)
        while i < j:
            while i < j and not ss[i].isalpha():
                i += 1
            while i < j and not ss[j].isalpha():
                j -= 1
            ss[i], ss[j] = ss[j], ss[i]
            i += 1
            j -= 1

        return "".join(ss)
