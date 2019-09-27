# -*- coding: utf-8 -*-

'''
https://leetcode-cn.com/problems/decode-string/

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
'''


class Solution:
    def decodeString(self, s: str) -> str:
        i, length = -1, len(s)
        n = 0
        stack = []

        while i < length-1:
            # print(stack)
            i += 1
            if '0' <= s[i] <= '9':
                n = (ord(s[i])-ord('0')) + n * 10
                continue

            if n > 0:
                stack.append(n)
                n = 0

            if s[i] == '[':
                continue
            elif s[i] == ']':
                self.pop_stack(stack)
            else:
                stack.append(s[i])

        return ''.join(stack)

    def pop_stack(self, stack):
        s = ''
        while stack:
            last = stack.pop()
            if isinstance(last, int):
                stack.append(s*last)
                return
            else:
                s = last+s


def main():
    s = Solution()
    print(s.decodeString(s="3[z]2[2[y]pq4[2[jk]e1[f]]]ef"))
    print(s.decodeString(s="3[ab2[cd]]"))
    print(s.decodeString(s="3[a]2[bc]"))
    print(s.decodeString(s="3[]2[bc]"))
    print(s.decodeString(s=""))
    print(s.decodeString(s="2[abc]3[cd]ef"))
    print(s.decodeString(s="3[a]2[b4[F]c]"))


if __name__ == '__main__':
    main()
