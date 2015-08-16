#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
learn from https://github.com/haoel/leetcode/blob/master/algorithms/palindromeNumber/palindromeNumber.cpp
"""

import unittest


class Solution:
    # @param {integer} x
    # @return {boolean}

    def isPalindrome(self, x):
        if x < 0:
            return False
        if x < 10:
            return True

        #10:10; 11:10; 123:100
        n = 1
        while(x/n >= 10):
            n*=10

        while(x):
            righti = x%10
            lefti = x/n
            if lefti != righti:
                return False
            x=x%n/10
            n/=100
        return True


class TestSolution(unittest.TestCase):

    def test_isPalindrome(self):
        s = Solution()

        self.assertEqual(True, s.isPalindrome(919))
        self.assertEqual(False, s.isPalindrome(1000021))
        self.assertEqual(True, s.isPalindrome(313))
        self.assertEqual(False, s.isPalindrome(-100))
        self.assertEqual(True, s.isPalindrome(0))
        self.assertEqual(False, s.isPalindrome(100))
        self.assertEqual(True, s.isPalindrome(111111))
        self.assertEqual(True, s.isPalindrome(1111111))
        self.assertEqual(True, s.isPalindrome(1110111))
        self.assertEqual(False, s.isPalindrome(123))

        import random
        for i in range(1000):
            x = random.randint(0,100000000000)
            rst = str(x) == str(x)[::-1]
            self.assertEqual(rst, s.isPalindrome(x))

        for i in range(1000):
            x = random.randint(0,100000)
            x = int(str(x)+str(x)[::-1])
            self.assertEqual(True, s.isPalindrome(x))


if __name__ == '__main__':
    unittest.main()
