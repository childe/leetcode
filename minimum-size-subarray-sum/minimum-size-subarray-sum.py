#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/minimum-size-subarray-sum/description/
"""


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        section_sum = 0
        left = right = 0
        min_len = len(nums) + 1
        while right < len(nums):
            # print(left, right, nums[left:right], section_sum, min_len)
            if section_sum < target:
                section_sum += nums[right]
                right += 1
            else:
                min_len = min(min_len, right - left)
                section_sum -= nums[left]
                left += 1
        while section_sum >= target:
            min_len = min(min_len, right - left)
            section_sum -= nums[left]
            left += 1
        return 0 if min_len == len(nums) + 1 else min_len


import unittest


class TestSolution(unittest.TestCase):
    def test_minSubArrayLen(self):
        solution = Solution()
        self.assertEqual(
            solution.minSubArrayLen(15, [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]), 2
        )
        self.assertEqual(solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]), 2)
        self.assertEqual(solution.minSubArrayLen(4, [1, 4, 4]), 1)
        self.assertEqual(solution.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]), 0)


if __name__ == "__main__":
    unittest.main()
