#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
"""
https://leetcode.com/problems/3sum-closest/


Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""


class Solution(object):

    def _threeSumClosest(self, nums, n, target):
        """
        :type nums: List[int]
        :type n: int
        :type target: int
        :rtype: int
        """
        if nums == []:
            return 0
        if nums[1:] == []:
            return nums[0]
        if n == 1:
            closest_diff = abs(nums[0] - target)
            for num in nums[1:]:
                if abs(num-target) < closest_diff:
                    closest_diff = abs(num-target)
                else:
                    return num
            return num

        closest = []
        for idx, num in enumerate(nums):
            if idx>0 and num==nums[idx-1]:
                continue
            closest.append(
                num +
                self._threeSumClosest(
                    nums[
                        :idx] +
                    nums[
                        idx +
                        1:],
                    n -
                    1,
                    target -
                    num))
        closest_diff = abs(closest[0]-target)
        rst = closest[0]
        for c in closest[1:]:
            if abs(c-target) < closest_diff:
                closest_diff = abs(c-target)
                rst = c
        return rst

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        return self._threeSumClosest(nums, 3, target)


class TestSolution(unittest.TestCase):

    def test_threeSumClosest(self):
        s = Solution()

        nums = [0,0,0]
        target = 1
        self.assertEqual(0, s.threeSumClosest(nums, target))

        nums = [-1, 2, 1, -4]
        target = 1
        self.assertEqual(2, s.threeSumClosest(nums, target))

        nums = [-3, -26, 43, 51, -70, -17, 31, 23]
        target = 289
        self.assertEqual(125, s.threeSumClosest(nums, target))

        import random
        import itertools
        nums = [random.randint(-100, 100)
                for e in range(random.randint(3, 10))]
        target = random.randint(0, 300)
        my_answer = s.threeSumClosest(nums, target)
        for e in itertools.combinations(nums, 3):
            self.assertTrue(abs(my_answer-target) <= abs(sum(e)-target))


if __name__ == '__main__':
    unittest.main()
