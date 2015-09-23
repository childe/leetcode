#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/roman-to-integer/

Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

基本字符
I V X L C D M
相应的阿拉伯数字表示为
1 5 10 50 100 500 1000

基本数字 Ⅰ、X 、C 中的任何一个、自身连用构成数目、或者放在大数的右边连用构成数目、都不能超过三个；放在大数的左边只能用一个；
不能把基本数字 V 、L 、D 中的任何一个作为小数放在大数的左边采用相减的方法构成数目；放在大数的右边采用相加的方式构成数目、只能使用一个；
V 和 X 左边的小数字只能用 Ⅰ；
L 和 C 左边的小数字只能用X；
D 和 M 左边的小数字只能用 C。
"""
import unittest


class Solution(object):

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        l = [d[e] for e in s]
        rst = 0
        for idx,e in enumerate(l):
            if idx<len(l)-1 and e < l[idx+1]:
                rst -= e
            else:
                rst += e

        return rst



class TestSolution(unittest.TestCase):

    def test_maxArea(self):
        s = Solution()

        self.assertEqual(s.romanToInt("I"), 1)
        self.assertEqual(s.romanToInt('III'), 3)
        self.assertEqual(s.romanToInt('IV'), 4)
        self.assertEqual(s.romanToInt('VI'), 6)
        self.assertEqual(s.romanToInt('VIII'), 8)
        self.assertEqual(s.romanToInt('IX'), 9)
        self.assertEqual(s.romanToInt('XI'), 11)
        self.assertEqual(s.romanToInt('LI'), 51)
        self.assertEqual(s.romanToInt('LXXVIII'), 78)
        self.assertEqual(s.romanToInt('LXXXVIII'), 88)
        self.assertEqual(s.romanToInt('XCVIII'), 98)
        self.assertEqual(s.romanToInt('CXI'), 111)
        self.assertEqual(s.romanToInt('CDXCIX'), 499)
        self.assertEqual(s.romanToInt('MDCLXVI'), 1666)
        self.assertEqual(s.romanToInt('MDCCCLXXXVIII'), 1888)

if __name__ == '__main__':
    unittest.main()
