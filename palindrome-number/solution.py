#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/palindrome-number/

Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.

Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.
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

        n = 0
        origin = x
        while(x > 0):
            x/=10
            n+=1
        x = origin

        i = 0
        while(i<=(n-1)/2):
            righti = (x-x%(10**i))/10**i%10
            lefti = (x-x%(10**(n-i-1)))/10**(n-i-1)%10
            if lefti != righti:
                return False
            i += 1
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
