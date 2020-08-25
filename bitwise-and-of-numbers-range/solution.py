# -*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/bitwise-and-of-numbers-range/

201. Bitwise AND of Numbers Range
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4
Example 2:

Input: [0,1]
Output: 0
"""


class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        r = m
        while r != 0 and m <= n:
            r &= m
            m = self.nextNum(m)

        return r

    def nextNum(self, i):
        offset = 0
        while i & 1 == 0:
            i = i >> 1
            offset += 1

        return (i + 1) << offset


def main():
    s = Solution()
    ans = s.rangeBitwiseAnd(600000000, 2147483645)
    print(ans)


if __name__ == "__main__":
    main()
