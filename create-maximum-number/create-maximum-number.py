#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
https://leetcode.cn/problems/create-maximum-number/
"""


class Solution:
    def maxNumber(self, nums1: list[int], nums2: list[int], k: int) -> list[int]:
        m, n = len(nums1), len(nums2)
        maxSubsequence = [0] * k
        start, end = max(0, k - n), min(k, m)

        for i in range(start, end + 1):
            subsequence1 = self.getMaxSubsequence(nums1, i)
            subsequence2 = self.getMaxSubsequence(nums2, k - i)
            curMaxSubsequence = self.merge(subsequence1, subsequence2)
            if self.compare(curMaxSubsequence, 0, maxSubsequence, 0) > 0:
                maxSubsequence = curMaxSubsequence

        return maxSubsequence

    def getMaxSubsequence(self, nums: list[int], k: int) -> list[int]:
        stack = [0] * k
        top = -1
        remain = len(nums) - k

        for num in nums:
            while top >= 0 and stack[top] < num and remain > 0:
                top -= 1
                remain -= 1
            if top < k - 1:
                top += 1
                stack[top] = num
            else:
                remain -= 1

        return stack

    def merge(self, subsequence1: list[int], subsequence2: list[int]) -> list[int]:
        x, y = len(subsequence1), len(subsequence2)
        if x == 0:
            return subsequence2
        if y == 0:
            return subsequence1

        mergeLength = x + y
        merged = list()
        index1 = index2 = 0

        for _ in range(mergeLength):
            if self.compare(subsequence1, index1, subsequence2, index2) > 0:
                merged.append(subsequence1[index1])
                index1 += 1
            else:
                merged.append(subsequence2[index2])
                index2 += 1

        return merged

    def compare(
        self, subsequence1: list[int], index1: int, subsequence2: list[int], index2: int
    ) -> int:
        x, y = len(subsequence1), len(subsequence2)
        while index1 < x and index2 < y:
            difference = subsequence1[index1] - subsequence2[index2]
            if difference != 0:
                return difference
            index1 += 1
            index2 += 1

        return (x - index1) - (y - index2)


import unittest


class TestSolution(unittest.TestCase):
    def test_maxNumber(self):
        solution = Solution()
        self.assertEqual(
            solution.maxNumber([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5), [9, 8, 6, 5, 3]
        )
        self.assertEqual(solution.maxNumber([6, 7], [6, 0, 4], 5), [6, 7, 6, 0, 4])
        self.assertEqual(solution.maxNumber([3, 9], [8, 9], 3), [9, 8, 9])


if __name__ == "__main__":
    # unittest.main()
    s = Solution()
    a = s.merge([3, 4, 6, 1], [9, 6, 2, 5, 8, 3])
    print(a)
