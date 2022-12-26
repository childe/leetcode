#!/usr/bin/env python

"""
https://leetcode.cn/problems/count-number-of-homogenous-substrings/

1759. 统计同构子字符串的数目
中等
39
相关企业
给你一个字符串 s ，返回 s 中 同构子字符串 的数目。由于答案可能很大，只需返回对 109 + 7 取余 后的结果。

同构字符串 的定义为：如果一个字符串中的所有字符都相同，那么该字符串就是同构字符串。

子字符串 是字符串中的一个连续字符序列。

 

示例 1：

输入：s = "abbcccaa"
输出：13
解释：同构子字符串如下所列：
"a"   出现 3 次。
"aa"  出现 1 次。
"b"   出现 2 次。
"bb"  出现 1 次。
"c"   出现 3 次。
"cc"  出现 2 次。
"ccc" 出现 1 次。
3 + 1 + 2 + 1 + 3 + 2 + 1 = 13
示例 2：

输入：s = "xy"
输出：2
解释：同构子字符串是 "x" 和 "y" 。
示例 3：

输入：s = "zzzzz"
输出：15
 

提示：

1 <= s.length <= 105
s 由小写字符串组成
"""


class Solution:
    def countHomogenous(self, s: str) -> int:
        """
        >>> s=Solution()
        >>> s.countHomogenous("abbcccaa")
        13
        >>> s.countHomogenous("xy")
        2
        >>> s.countHomogenous("zzzzz")
        15
        >>> s.countHomogenous("x")
        1
        >>> s.countHomogenous("xx")
        3
        """
        i, j, l, ans = 0, 0, len(s), 0

        def f(i: int):
            """
            >>> f(1)
            1
            >>> f(2)
            3
            >>> f(3):
            6
            >>> f(5)
            15
            """
            return (i + 1) * i // 2

        while j < l:
            while j < l and s[j] == s[i]:
                j += 1
            ans += f(j - i)
            i = j

        return ans % (10**9 + 7)
