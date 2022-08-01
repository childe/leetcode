#!/usr/bin/env python3
"""
https://leetcode.cn/problems/valid-square/

p1.length == p2.length == p3.length == p4.length == 2
-10^4 <= xi, yi <= 10^4
"""


class Solution:
    def validSquare(
        self, p1: list[int], p2: list[int], p3: list[int], p4: list[int]
    ) -> bool:
        """
        >>> s = Solution()
        >>> s.validSquare(p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1])
        True
        >>> s.validSquare(p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12])
        False
        >>> s.validSquare(p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1])
        True
        """

        orderedPoints = [[]] * 4
        points = [p1, p2, p3, p4]
        min_left = min([e[0] for e in points])
        l1 = [e for e in points if e[0] == min_left]
        max_left = max([e[0] for e in points])
        l2 = [e for e in points if e[0] == max_left]
        max_up = max([e[1] for e in points])
        l3 = [e for e in points if e[1] == max_up]
        min_up = min([e[1] for e in points])
        l4 = [e for e in points if e[1] == min_up]
        if len(l1) == 1:
            if len(l2) > 1 or len(l3) > 1 or len(l4) > 1:
                ##print(1)
                return False
            orderedPoints = [l1[0], l3[0], l2[0], l4[0]]
        elif len(l1) == 2:
            if len(l2) != 2 or len(l3) != 2 or len(l4) != 2:
                ##print(2)
                return False
            l1.sort(key=lambda x: x[1])
            orderedPoints[:2] = l1
            l2.sort(key=lambda x: -x[1])
            orderedPoints[-2:] = l2
        else:
            ##print(3)
            return False

        ##print(orderedPoints)
        p1, p2, p3, p4 = orderedPoints
        if (p1[0] - p2[0]) * (p3[1] - p4[1]) != (p3[0] - p4[0]) * (p1[1] - p2[1]):
            ##print(4)
            return False
        if (p1[0] - p4[0]) * (p2[1] - p3[1]) != (p2[0] - p3[0]) * (p1[1] - p4[1]):
            ##print(5)
            return False
        if (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 != (p3[0] - p2[0]) ** 2 + (
            p3[1] - p2[1]
        ) ** 2:
            ##print(6)
            return False
        return True
