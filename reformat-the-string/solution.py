#!/usr/bin/env python3

"""
https://leetcode.cn/problems/reformat-the-string/
"""


class Solution:
    def reformat(self, s: str) -> str:
        """
        >>> s=Solution()
        >>> s.reformat("a0b1c2")
        "0a1b2c"
        >>> s.reformat("leetcode")
        ""
        >>> s.reformat("1229857369")
        ""
        >>> s.reformat("covid2019")
        "c2o0v1i9d"
        >>> s.reformat("ab123")
        "1a2b3"
        """
        alphabet = ""
        num = ""
        for c in s:
            if "a" <= c <= "z":
                alphabet += c
            else:
                num += c
        d = len(alphabet) - len(num)
        if d > 1 or d < -1:
            return ""

        ans = ""
        while alphabet and num:
            ans += alphabet[0]
            alphabet = alphabet[1:]
            ans += num[0]
            num = num[1:]
        if alphabet:
            ans += alphabet[0]
        if num:
            ans = num[0] + ans
        return ans
