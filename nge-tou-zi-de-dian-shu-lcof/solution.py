#!/usr/bin/env python

"""
https://leetcode.cn/problems/nge-tou-zi-de-dian-shu-lcof/description/

把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。

 

你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。

 

示例 1:

输入: 1
输出: [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]
示例 2:

输入: 2
输出: [0.02778,0.05556,0.08333,0.11111,0.13889,0.16667,0.13889,0.11111,0.08333,0.05556,0.02778]

限制：
1 <= n <= 11
"""

from functools import lru_cache

@lru_cache
def a(target, n):
    """
    >>> a(1, 1)
    1
    >>> a(1, 2)
    0
    >>> a(2, 1)
    1
    >>> a(3, 2)
    2
    """
    if target <= 0 or n <= 0:
        return 0
    if target < n or target > 6 * n:
        return 0
    if n == 1:
        return 1
    ans = 0
    for i in range(1, 7):
        ans += a(target - i, n - 1)
    return ans


class Solution:
    def dicesProbability(self, n: int) -> list[float]:
        """
        >>> s=Solution()
        >>> s.dicesProbability(1)
        [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]
        """
        min_value, max_valu = n, n * 6
        v: list[int] = []
        for i in range(min_value, max_valu + 1):
            v.append(a(i, n))

        total = sum(v)
        return [i / total for i in v]

Solution().dicesProbability(10)
