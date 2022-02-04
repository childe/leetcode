#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/longest-nice-substring/

1763. Longest Nice Substring
A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase. For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b' appears, but 'B' does not.

Given a string s, return the longest substring of s that is nice. If there are multiple, return the substring of the earliest occurrence. If there are none, return an empty string.

 

Example 1:

Input: s = "YazaAay"
Output: "aAa"
Explanation: "aAa" is a nice string because 'A/a' is the only letter of the alphabet in s, and both 'A' and 'a' appear.
"aAa" is the longest nice substring.

Example 2:

Input: s = "Bb"
Output: "Bb"
Explanation: "Bb" is a nice string because both 'B' and 'b' appear. The whole string is a substring.

Example 3:

Input: s = "c"
Output: ""
Explanation: There are no nice substrings.
 

Constraints:

1 <= s.length <= 100
s consists of uppercase and lowercase English letters.
"""


class Solution:
    def isNiceLetter(self, c: str, s: str) -> bool:
        if c.islower():
            return c.upper() in s
        return c.lower() in s

    def longestNiceSubstring(self, s: str) -> str:
        """
        >>> s = Solution()
        >>> s.longestNiceSubstring(s = "YazaAay")
        'aAa'
        >>> s.longestNiceSubstring(s = "Bb")
        'Bb'
        >>> s.longestNiceSubstring(s = "c")
        ''
        """
        if s == "":
            return ""

        for i, c in enumerate(s):
            if not self.isNiceLetter(c, s):
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i + 1 :])

                if len(left) >= len(right):
                    return left
                else:
                    return right
        return s


def main():
    s = Solution()
    ans = s.longestNiceSubstring(s="YazaAay")
    print(ans)


if __name__ == "__main__":
    main()
