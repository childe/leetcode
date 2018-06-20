#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/powx-n/description/

Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2^^-2 = (1/2)^^2 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−2^^31, 2^^31 − 1]
'''

import math


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        >>> s = Solution()
        >>> s.myPow(2.00000, 10) == math.pow(2.00000, 10)
        True
        >>> s.myPow(2.10000, 3) == math.pow(2.10000, 3)
        True
        >>> s.myPow(2.00000, -2) == math.pow(2.00000, -2)
        True
        """
        if n == 0:
            return 1
        if n < 0:
            return 1/self.myPow(x, -n)

        remainder = 1
        while n > 1:
            x, n, remainder = x*x, n/2, remainder * x if n % 2 else remainder

        return x*remainder
