#!
# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/problems/longest-happy-string/

1405. Longest Happy String
A string s is called happy if it satisfies the following conditions:

s only contains the letters 'a', 'b', and 'c'.
s does not contain any of "aaa", "bbb", or "ccc" as a substring.
s contains at most a occurrences of the letter 'a'.
s contains at most b occurrences of the letter 'b'.
s contains at most c occurrences of the letter 'c'.
Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.

Example 2:

Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It is the only correct answer in this case.
 

Constraints:

0 <= a, b, c <= 100
a + b + c > 0
"""


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        """
        >>> s = Solution()
        >>> s.longestDiverseString(1, 1, 7)
        'ccaccbcc'
        >>> s.longestDiverseString(7, 1, 0)
        'aabaa'
        """
        res = []

        candidates = [[a, "a"], [b, "b"], [c, "c"]]
        while True:
            # print(f"{candidates=}")
            # print(f"{prefix=}")
            candidates.sort(key=lambda x: (x[0], -ord(x[1])), reverse=True)
            m = candidates[0]
            _, c = m
            if res[-2:] == [c, c]:
                m = candidates[1]
            count, c = m

            if count == 0:
                break

            res.append(c)
            m[0] -= 1

            # print(f"{res=}")

        return "".join(res)
