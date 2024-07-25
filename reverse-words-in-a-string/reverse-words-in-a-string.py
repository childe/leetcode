# -*- coding: utf-8 -*-
"""
https://leetcode.cn/problems/reverse-words-in-a-string/
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])


def main():
    s = Solution()
    print(s.reverseWords("the sky is blue"))
    print(s.reverseWords("  hello world  "))
    print(s.reverseWords("a good   example"))


if __name__ == "__main__":
    main()
