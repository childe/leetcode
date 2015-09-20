#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/integer-to-roman/

Given an integer, convert it to a roman numeral.

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
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        d = {0:'',1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}

        if num in d:
            return d[num]

        origin = num
        i = 1
        while(num>=10):
            i*=10
            num /= 10

        if num==9:
            a,b = 1,10
        elif num>=5:
            a,b = 5,num-5
        elif num==4:
            a,b = 1,5
        else:
            a,b = 0,num

        if a == 0:
            return b*d[i] + self.intToRoman(origin-b*i)

        a*=i
        b*=i
        return self.intToRoman(a)+self.intToRoman(b)+self.intToRoman(origin-num*i)


class TestSolution(unittest.TestCase):

    def test_maxArea(self):
        s = Solution()

        self.assertEqual(s.intToRoman(1), 'I')
        self.assertEqual(s.intToRoman(3), 'III')
        self.assertEqual(s.intToRoman(4), 'IV')
        self.assertEqual(s.intToRoman(6), 'VI')
        self.assertEqual(s.intToRoman(8), 'VIII')
        self.assertEqual(s.intToRoman(9), 'IX')
        self.assertEqual(s.intToRoman(11), 'XI')
        self.assertEqual(s.intToRoman(51), 'LI')
        self.assertEqual(s.intToRoman(78), 'LXXVIII')
        self.assertEqual(s.intToRoman(88), 'LXXXVIII')
        self.assertEqual(s.intToRoman(98), 'XCVIII')
        self.assertEqual(s.intToRoman(111), 'CXI')
        self.assertEqual(s.intToRoman(499), 'CDXCIX')
        self.assertEqual(s.intToRoman(1666), 'MDCLXVI')
        self.assertEqual(s.intToRoman(1888), 'MDCCCLXXXVIII')

if __name__ == '__main__':
    unittest.main()
