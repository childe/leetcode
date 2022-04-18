#!/usr/bin/env python3
"""
https://leetcode-cn.com/problems/lexicographical-numbers/

给你一个整数 n ，按字典序返回范围 [1, n] 内所有整数。

你必须设计一个时间复杂度为 O(n) 且使用 O(1) 额外空间的算法。

 

示例 1：

输入：n = 13
输出：[1,10,11,12,13,2,3,4,5,6,7,8,9]
示例 2：

输入：n = 2
输出：[1,2]
 

提示：

1 <= n <= 5 * 104
"""


class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        """
        >>> s = Solution()
        >>> s.lexicalOrder(13)
        [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]
        >>> s.lexicalOrder(2)
        [1, 2]
        """
        ans = []
        i = 1

        while i <= n:
            # print(i)
            ans.append(i)
            if i * 10 <= n:
                i *= 10
                continue

            if i % 10 != 9:
                if i < n:
                    i += 1
                    continue
                else:
                    i = i // 10 + 1
            else:
                i += 1

            while i % 10 == 0:
                i //= 10

            if i == 1:
                break

        return ans


s = Solution()
s.lexicalOrder(13)
