#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
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
        >>> s.divide(10,-3)
        -3
        >>> s.divide(-10,3)
        -3
        """

        MAX_INT = 0xffffffff >> 1

        rst = 0
        factor = 1
        if dividend < 0:
            factor = -factor
            dividend = -dividend
        if divisor < 0:
            factor = -factor
            divisor = -divisor

        while True:
            if dividend == divisor:
                result = rst + 1
                if result >  MAX_INT:
                    return MAX_INT
                return result * factor
            if dividend < divisor:
                result = rst
                if result >  MAX_INT:
                    return MAX_INT
                return result * factor

            bottom = 1
            value = divisor
            while(value < dividend):
                value = divisor << bottom

                if value == dividend:
                    result = rst + (1 << bottom)
                    if result >  MAX_INT:
                        return MAX_INT
                    return result * factor
                elif value > dividend:
                    bottom >>= 1
                    rst += (1 << bottom)
                    dividend -= (divisor << bottom)
                else:
                    bottom <<= 1
