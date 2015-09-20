#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/container-with-most-water/

Given n non-negative integers a1, a2, ..., an, where each represents a point
at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis
forms a container, such that the container contains the most water.

Note: You may not slant the container.
"""
import unittest


class Solution(object):

    def maxArea2(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        most = 0
        for idx, h in enumerate(height):
            for ridx, rh in enumerate(height[idx:]):
                most = max(ridx*min(h, rh), most)
                # print h, rh, most

        return most

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        if not height[1:]:
            return 0

        left = 0
        right = len(height)-1
        most = 0
        while(left < right):
            most = max(most, min(height[left], height[right])*(right-left))
            if height[left] < height[right]:
                while(left < right and height[left] >= height[left+1]):
                    left += 1
                else:
                    left += 1
            else:
                while(left < right and height[right] >= height[right-1]):
                    right -= 1
                else:
                    right -= 1

        return most


class TestSolution(unittest.TestCase):

    def test_maxArea(self):
        s = Solution()

        for l in open("testcase").readlines():
            l = l.strip()
            if l == "":
                 continue
            l = [int(e) for e in l.split(",")]
            self.assertEqual(s.maxArea(l), s.maxArea2(l))
            #self.assertEqual(s.maxArea(l), 48267879)

        self.assertEqual(0, s.maxArea([]))

        import random
        for i in range(1000):
            l = []
            for j in range(random.randint(1, 10)):
                l.append(random.randint(1, 10000))
            self.assertEqual(s.maxArea(l), s.maxArea2(l))


if __name__ == '__main__':
    unittest.main()
