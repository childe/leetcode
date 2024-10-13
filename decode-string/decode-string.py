#!/usr/bin/env python3

"""
https://leetcode.cn/problems/decode-string/description/
"""


class Solution:
    def findClosingBracket(self, s: str, start: int) -> int:
        stack = []
        for i in range(start, len(s)):
            if s[i] == "[":
                stack.append("[")
            elif s[i] == "]":
                stack.pop()
                if not stack:
                    return i
        raise Exception("No closing bracket found")

    def decodeString(self, s: str) -> str:
        # print(s)
        ans = ""
        num = ""
        i = -1
        while (i + 1) < len(s):
            i += 1
            c = s[i]
            if c.isdigit():
                num += c
            elif c == "[":
                e = self.findClosingBracket(s, i)
                n = int(num) if num else 1
                ans += self.decodeString(s[i + 1 : e]) * n
                i = e
                num = ""
            else:
                ans += c
        return ans


import unittest


class TestSolution(unittest.TestCase):

    def test_decodeString(self):
        solution = Solution()
        self.assertEqual(solution.decodeString("3[a]2[bc]"), "aaabcbc")
        self.assertEqual(solution.decodeString("3[a2[c]]"), "accaccacc")
        self.assertEqual(solution.decodeString("2[abc]3[cd]ef"), "abcabccdcdcdef")
        self.assertEqual(solution.decodeString("100[leetcode]"), "leetcode" * 100)


if __name__ == "__main__":
    unittest.main()
