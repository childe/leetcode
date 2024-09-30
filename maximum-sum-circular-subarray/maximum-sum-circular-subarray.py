#!/usr/bin/env python3

"""
https://leetcode.cn/problems/maximum-sum-circular-subarray/description/
"""


class Solution:
    def maxSubarraySumCircular1(self, nums: list[int]) -> int:
        c = 0
        r = nums[0]
        for n in nums:
            c += n
            r = max(r, c)
            if c <= 0:
                c = 0

        return r

    def maxSubarraySumCircular2(self, nums: list[int]) -> int:
        clockwise = []
        for n in nums[1:]:
            clockwise.append(clockwise[-1] + n if clockwise else n)
        print("clockwise", clockwise)
        max_clockwise = [clockwise[0]]
        for n in clockwise[1:]:
            max_clockwise.append(max(n, max_clockwise[-1]))
        # print("max_clockwise", max_clockwise)

        anticlockwise = []
        for n in nums[:0:-1]:
            anticlockwise.append(anticlockwise[-1] + n if anticlockwise else n)
        # print("anticlockwise", anticlockwise)
        max_anticlockwise = [anticlockwise[0]]
        for n in anticlockwise[1:]:
            max_anticlockwise.append(max(n, max_anticlockwise[-1]))
        # print("max_anticlockwise", max_anticlockwise)

        r = 0
        for i, n in enumerate(max_clockwise[:-1]):
            r = max(r, max(0, max_clockwise[i]) + max(0, max_anticlockwise[-(2 + i)]))
        r = max(r, max_clockwise[-1])
        # print("r,", r)
        return r + nums[0]

    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(
            self.maxSubarraySumCircular1(nums), self.maxSubarraySumCircular2(nums)
        )


import unittest


class TestSolution(unittest.TestCase):
    def test_maxSubarraySumCircular(self):
        solution = Solution()
        self.assertEqual(solution.maxSubarraySumCircular([-2, 1]), 1)
        self.assertEqual(solution.maxSubarraySumCircular([-2, -1]), -1)
        self.assertEqual(solution.maxSubarraySumCircular([-2]), -2)
        self.assertEqual(solution.maxSubarraySumCircular([5, -3, 5]), 10)
        self.assertEqual(solution.maxSubarraySumCircular([1, -2, 3, -2]), 3)
        self.assertEqual(solution.maxSubarraySumCircular([3, -1, 2, -1]), 4)
        self.assertEqual(solution.maxSubarraySumCircular([3, -2, 2, -3]), 3)
        self.assertEqual(solution.maxSubarraySumCircular([-2, -3, -1]), -1)


if __name__ == "__main__":
    unittest.main()
