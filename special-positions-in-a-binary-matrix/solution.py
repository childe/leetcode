#!/usr/bin/env python3


"""
https://leetcode.cn/problems/special-positions-in-a-binary-matrix/
"""


class Solution:
    def numSpecial(self, mat: list[list[int]]) -> int:
        """
        >>> s = Solution()
        >>> s.numSpecial([[1,0,0],[0,0,1],[1,0,0]])
        1
        """
        ans = 0
        col_cache = {}
        for row in mat:
            # print(row)
            ones = []
            for i, n in enumerate(row):
                if n == 1:
                    ones.append(i)
            # print(ones)
            if len(ones) == 1:
                j = ones[0]
                cols = [row[j] for row in mat]
                s = col_cache.get(j, sum(cols))
                col_cache[j] = s
                if s == 1:
                    ans += 1
        return ans
