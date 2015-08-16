#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/reverse-integer/
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Have you thought about this?
Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!

If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?

For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

Update (2014-11-10):
Test cases had been added to test the overflow behavior.
"""

import unittest


class Solution:
    # @param {integer} x
    # @return {integer}

    def reverse(self, x):
        if x == 0:
            return 0
        if x > 0:
            r = int(str(x)[::-1].lstrip("0"))
            if r > 0xFFFFFFFF/2-1:
                return 0
            return r
        else:
            r = -1*int(str(x)[1:][::-1].lstrip("0"))
            if r < -0xFFFFFFFF/2:
                return 0
            return r


class TestSolution(unittest.TestCase):

    def test_reverse(self):
        s = Solution()

        x = 123
        self.assertEqual(321, s.reverse(x))

        x = -123
        self.assertEqual(-321, s.reverse(x))

        x = 0
        self.assertEqual(0, s.reverse(x))

        x = 1534236469
        self.assertEqual(0, s.reverse(x))


if __name__ == '__main__':
    unittest.main()
