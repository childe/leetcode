#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/divide-two-integers/#/description

Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
"""


class Solution(object):

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        >>> s = Solution()
        >>> s.divide(10,3)
        3
        >>> s.divide(9,3)
        3
        >>> s.divide(99,3)
        33
        >>> s.divide(99,10)
        9
        >>> s.divide(16,2)
        8
        >>> s.divide(32,2)
        16
        >>> s.divide(100000000,1)
        100000000
        >>> s.divide(100000000000000000000000,1)
        2147483647
        >>> s.divide(-100000000000000000000000,1)
        -2147483648
        >>> s.divide(10,-3)
        -3
        >>> s.divide(-10,3)
        -3
        """

        rst = 0
        factor = (dividend > 0) is (divisor > 0)
        if dividend < 0:
            dividend = -dividend
        if divisor < 0:
            divisor = -divisor

        while dividend >= divisor:
            c, b = 0, divisor
            while dividend >= b:
                c += 1
                b <<= 1
            rst += 1 << (c-1)
            dividend -= b >> 1
        if not factor:
            rst = -rst
        return min(2147483647, max(-2147483648, rst))
