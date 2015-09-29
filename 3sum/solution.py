#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/3sum/

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
"""
import unittest


class Solution(object):

    def _threeSum(self, nums, n, s):
        """
        :type nums: List[int]
        :type n: int, how much num
        :type s: int, sum
        :rtype: List[List[int]]
        """
        if nums == []:
            return []
        if n == 1:
            if s in nums:
                return [[s]]
            return []

        rst = []
        for i, e in enumerate(nums):
            if i > 0 and e == nums[i-1]:
                continue
            for r in self._threeSum(nums[i+1:], n-1, s-e):
                rst.append([e]+r)
        return rst

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        return self._threeSum(nums, 3, 0)


class TestSolution(unittest.TestCase):

    def test_threeSum(self):
        s = Solution()

        nums = []
        self.assertEqual([],s.threeSum(nums))
        nums = [1,2,3,4]
        self.assertEqual([],s.threeSum(nums))

        nums = [-1, 0, 1, 2, -1, -4]
        answer = [[-1, 0, 1], [-1, -1, 2]]
        for e in answer:
            self.assertTrue(e in s.threeSum(nums))


        import random
        nums = [random.randint(-100, 100)
                for e in range(random.randint(0, 100))]
        my_answer = s.threeSum(nums)
        for e in my_answer:
            self.assertEqual(0, sum(e))
            self.assertEqual(3, len(e))

if __name__ == '__main__':
    unittest.main()
