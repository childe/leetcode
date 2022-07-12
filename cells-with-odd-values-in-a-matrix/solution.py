#!/usr/bin/env python3
"""
https://leetcode.cn/problems/cells-with-odd-values-in-a-matrix/
Constraints:

1 <= m, n <= 50
1 <= indices.length <= 100
0 <= ri < m
0 <= ci < n
 

Follow up: Could you solve this in O(n + m + indices.length) time with only O(n + m) extra space?
"""


class Solution:
    def oddCells(self, m: int, n: int, indices: list[list[int]]) -> int:
        """
        >>> s= Solution()
        >>> s.oddCells(m = 2, n = 3, indices = [[0,1],[1,1]])
        6
        >>> s.oddCells(m = 2, n = 2, indices = [[1,1],[0,0]])
        0
        """
        rows = set()
        cols = set()
        for i, j in indices:
            if i in rows:
                rows.remove(i)
            else:
                rows.add(i)

            if j in cols:
                cols.remove(j)
            else:
                cols.add(j)

        ans = 0
        ans += len(rows) * n
        ans += len(cols) * m
        ans -= 2 * len(rows) * len(cols)
        return ans
