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
        >>> s.divide(100,3)
        33
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
        factor = 1
        if dividend < 0:
            factor = -factor
            dividend = -dividend
        if divisor < 0:
            factor = -factor
            divisor = -divisor

        c = 0
        rest = dividend
        b = divisor
        while rest >= divisor:
            c += 1
            b = divisor << c
            if b > rest:
                rst += 1 << (c-1)
                c = 0
                rest -= b >> 1
                b = divisor
        rst = rst*factor
        return min(2147483647, max(-2147483648, rst))
