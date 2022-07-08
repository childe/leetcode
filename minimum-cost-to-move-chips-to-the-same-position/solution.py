#!/usr/bin/env python3

"""
https://leetcode.cn/problems/minimum-cost-to-move-chips-to-the-same-position/

1 <= position.length <= 100
1 <= position[i] <= 10^9
"""


class Solution:
    def minCostToMoveChips(self, position: list[int]) -> int:
        """
        >>> s=Solution()
        >>> s.minCostToMoveChips(position = [1,2,3])
        1
        >>> s.minCostToMoveChips(position = [2,2,2,3,3])
        2
        >>> s.minCostToMoveChips(position = [1,1000000000])
        1
        """
        p0_count, p1_count = 0, 0
        for p in position:
            if p % 2 == 0:
                p0_count += 1
            else:
                p1_count += 1
        return min(p0_count, p1_count)
