#!/usr/bin/env python3
"""
https://leetcode.cn/problems/one-away-lcci/

字符串有三种编辑操作:插入一个字符、删除一个字符或者替换一个字符。 给定两个字符串，编写一个函数判定它们是否只需要一次(或者零次)编辑。

 

示例 1:

输入: 
first = "pale"
second = "ple"
输出: True
 

示例 2:

输入: 
first = "pales"
second = "pal"
输出: False

"""


class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        """
        >>> s = Solution()
        >>> s.oneEditAway("pale","ple")
        True
        >>> s.oneEditAway("pales","ple")
        False
        >>> s.oneEditAway("","a")
        True
        >>> s.oneEditAway("a","ab")
        True
        >>> s.oneEditAway("ab","a")
        True
        """
        m, n = len(first), len(second)
        if abs(m - n) >= 2:
            return False

        if m == n:
            s = [first[i] != second[i] for i in range(m)]
            return sum(s) <= 1

        if m < n:
            first, second = second, first

        i = 0
        for i in range(len(second)):
            if first[i] == second[i]:
                continue
            else:
                break
        else:
            return True
        # print(first, second)
        # print(i)
        # print(first[1 + i :], second[i:])
        return first[i + 1 :] == second[i:]
