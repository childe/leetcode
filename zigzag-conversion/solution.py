#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/zigzag-conversion/
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
    (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""

import unittest

class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        """
        每个Z字有2*numRows-2个字符
        idx个字符位于第idx / (2*numRows-2)个Z字 (index从0开始), 是这个Z字的idx % (2*numRows-2)的字符
        """
        if numRows == 1:
            return s

        rst = []
        for idx,e in enumerate(s):
            #print
            #print idx,e
            z_idx = idx / (2*numRows -2)
            z_inner_idx = idx % (2*numRows -2)

            inner_row = z_inner_idx if z_inner_idx < numRows else (2*numRows-z_inner_idx-2)
            inner_col = 0 if z_inner_idx < numRows else (z_inner_idx-numRows+1)
            #print "inner", inner_row, inner_col
            row = inner_row
            col = z_idx * (numRows-1) + inner_col
            #print row,col
            rst.append( ((row,col), e) )

        rst.sort(key=lambda e:e[0])
        return "".join([e[1] for e in rst])


class TestSolution(unittest.TestCase):
    def test_convert(self):
        s = Solution()
        rst = s.convert("PAYPALISHIRING", 3)
        self.assertEqual("PAHNAPLSIIGYIR", rst)

        rst = s.convert("A", 1)
        self.assertEqual("A", rst)

        rst = s.convert("ABCDE", 4)
        self.assertEqual("ABCED", rst)

if __name__ == '__main__':
    unittest.main()
