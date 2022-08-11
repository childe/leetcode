#!/usr/bin/env python3

"""
https://leetcode.cn/problems/reformat-the-string/
"""

from collections import deque


class Solution:
    def reformat(self, s: str) -> str:
        """
        >>> s=Solution()
        >>> s.reformat("a0b1c2")
        'a0b1c2'
        >>> s.reformat("leetcode")
        ''
        >>> s.reformat("1229857369")
        ''
        >>> s.reformat("covid2019")
        'c2o0v1i9d'
        >>> s.reformat("ab123")
        '3a1b2'
        """
        ans = ""
        alphabet = deque()
        num = deque()
        state = 0
        for c in s:
            if "a" <= c <= "z":
                if state != 1:
                    ans += c
                    state = 1
                    if num:
                        ans += num.popleft()
                        state = 2
                else:
                    alphabet.append(c)
            else:
                if state != 2:
                    ans += c
                    state = 2
                    if alphabet:
                        ans += alphabet.popleft()
                        state = 1
                else:
                    num.append(c)

        if len(alphabet) > 1 or len(num) > 1:
            return ""

        if alphabet:
            if "a" <= ans[0] <= "z":
                return ""
            return alphabet.popleft() + ans
        if num:
            if "0" <= ans[0] <= "9":
                return ""
            return num.popleft() + ans

        return ans
