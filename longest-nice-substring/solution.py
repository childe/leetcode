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
        Z = ord("Z")

        def normalize(x):
            return x if x <= Z else -x + 32

        m = {}
        for c in s:
            m[normalize(ord(c))] = True
        # print(m)

        flags = [1 if m.get(-normalize(ord(c)), False) else 0 for c in s]
        # print(flags)

        i, j, l, max_length = 0, 0, len(flags), 0
        start, end = 0, 0
        flags.append(2)
        while j < l:
            i = j
            while flags[j] == 1:
                j += 1
            if j - i > max_length:
                max_length = j - i
                start, end = i, j
                i = j
            while flags[j] == 0:
                j += 1

        return s[start:end]


def main():
    s = Solution()
    ans = s.longestNiceSubstring(s="YazaAay")
    print(ans)


if __name__ == "__main__":
    main()
