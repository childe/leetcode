#!/usr/bin/env python3

"""
https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/description/
"""


class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        ans = 0
        if points == []:
            return 0
        points.sort(key=lambda x: x[0])
        interval = [points[0][0] - 1, points[0][0] - 1]

        for p in points:
            if p[0] <= interval[1]:
                interval = p[0], min(interval[1], p[1])
            else:
                interval = p
                ans += 1

        return ans


import unittest


class TestSolution(unittest.TestCase):
    def test_findMinArrowShots(self):
        solution = Solution()
        self.assertEqual(
            solution.findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]), 2
        )
        self.assertEqual(
            solution.findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]]), 4
        )
        self.assertEqual(
            solution.findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]), 2
        )


if __name__ == "__main__":
    unittest.main()
