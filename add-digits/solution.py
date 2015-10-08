#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/add-digits/

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?

Hint:

A naive implementation of the above process is trivial. Could you come up with other methods? Show More Hint
Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
"""
import unittest


class Solution(object):

    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        rst = num % 9
        return rst if rst > 0 else 9


class TestSolution(unittest.TestCase):

    def test_addDigits(self):
        s = Solution()

        import random
        for num in range(10):
            while(num >= 10):
                num = num/10 + num % 10
            self.assertEqual(num, s.addDigits(num))

        for i in range(1000):
            num = random.randint(1, 10**9)
            print num
            while(num >= 10):
                num = num/10 + num % 10
            self.assertEqual(num, s.addDigits(num))


if __name__ == '__main__':
    unittest.main()
