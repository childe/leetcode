#!/usr/bin/env python3

"""
https://leetcode.cn/problems/rank-transform-of-an-array/

0 <= arr.length <= 10^5
-10^9 <= arr[i] <= 10^9
"""


class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        """
        >>> s = Solution()
        >>> s.arrayRankTransform(arr = [40,10,20,30])
        [4, 1, 2, 3]
        >>> s.arrayRankTransform(arr = [100,100,100])
        [1, 1, 1]
        >>> s.arrayRankTransform(arr = [37,12,28,9,100,56,80,5,12])
        [5, 3, 4, 2, 8, 6, 7, 1, 3]
        """
        m = {}
        for i, n in enumerate(sorted(list(set(arr)))):
            if n not in m:
                m[n] = i + 1
        ans = []
        for n in arr:
            ans.append(m[n])
        return ans
