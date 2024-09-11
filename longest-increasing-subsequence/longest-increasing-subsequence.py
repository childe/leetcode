#!/usr/bin/env python3
"""
https://leetcode.cn/problems/longest-increasing-subsequence/
"""


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        c = (
            []
        )  # 存储已经遍历过的数字的最长递增子序列的结果。c[i] 是 nums[i] 作为最后一个元素, 且包含nums[i]的最长递增子序列的长度
        for i, n in enumerate(nums):
            # 将 nums[i] 插入到 c 中
            r = 1
            for j, v in enumerate(nums[:i]):
                if v < n:
                    r = max(r, c[j] + 1)
            c.append(r)

        return max(c)


import unittest


class TestSolution(unittest.TestCase):
    def test_lengthOfLIS(self):
        solution = Solution()
        self.assertEqual(solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]), 4)
        self.assertEqual(solution.lengthOfLIS([0, 1, 0, 3, 2, 3]), 4)
        self.assertEqual(solution.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]), 1)


if __name__ == "__main__":
    unittest.main()
