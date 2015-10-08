#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
"""
https://leetcode.com/problems/house-robber/

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Credits:
Special thanks to @ifanchu for adding this problem and creating all test cases. Also thanks to @ts for adding additional test cases.
"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if nums == []:
            return 0
        if nums[1:] == []:
            return nums[0]
        if nums[2:] == []:
            return max(nums)

        mid = len(nums)/2
        if_rob_mid = nums[mid] + self.rob(nums[:mid-1]) + self.rob(nums[mid+2:])
        if_not_rob_mid = self.rob(nums[:mid]) + self.rob(nums[mid+1:])
        return max(if_rob_mid,if_not_rob_mid)


class TestSolution(unittest.TestCase):
    def test_rob(self):
        s = Solution()

        nums = []
        answer = 0
        my_answer = s.rob(nums)
        self.assertEqual(answer, my_answer)

        nums = [1]
        answer = 1
        my_answer = s.rob(nums)
        self.assertEqual(answer, my_answer)

        nums = [1,2]
        answer = 2
        my_answer = s.rob(nums)
        self.assertEqual(answer, my_answer)

        nums = [1,2,3]
        answer = 4
        my_answer = s.rob(nums)
        self.assertEqual(answer, my_answer)

        nums = [1,2,3,4]
        answer = 6
        my_answer = s.rob(nums)
        self.assertEqual(answer, my_answer)


if __name__ == '__main__':
    unittest.main()
