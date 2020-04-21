# -*- coding: utf-8 -*-


'''
https://leetcode-cn.com/problems/minimum-window-substring/

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
'''


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """


def main():
    s = Solution()

    S = "ADOBECODEBANC"
    T = "ABC"
    ans = s.minWindow(S, T)
    assert T in ans


if __name__ == '__main__':
    main()
