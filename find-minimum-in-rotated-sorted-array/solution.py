#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
"""
import unittest


class Solution(object):

    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return None

        start = 0
        end = len(nums)-1
        while(start < end-1):
            mid = (start+end)/2
            if nums[mid] < nums[end]:
                end = mid
            else:
                start = mid
        return min(nums[start:end+1])


class testSolution(unittest.TestCase):

    def test_findMin(self):
        s = Solution()

        nums = []
        self.assertEqual(None, s.findMin(nums))

        nums = [1]
        self.assertEqual(1, s.findMin(nums))

        nums = [1, 2]
        self.assertEqual(1, s.findMin(nums))

        nums = [2, 1]
        self.assertEqual(1, s.findMin(nums))

        nums = [1, 2, 3]
        self.assertEqual(1, s.findMin(nums))

        nums = [2, 3, 1]
        self.assertEqual(1, s.findMin(nums))

        nums = [3, 1, 2]
        self.assertEqual(1, s.findMin(nums))

        nums = [2, 3, 4, 1]
        self.assertEqual(1, s.findMin(nums))

        nums = [3, 4, 1, 2]
        self.assertEqual(1, s.findMin(nums))

        nums = [4, 1, 2, 3]
        self.assertEqual(1, s.findMin(nums))

        nums = range(100)
        for i in range(len(nums)):
            self.assertEqual(0, s.findMin(nums[i:] + nums[:i]))
        nums = range(101)
        for i in range(len(nums)):
            self.assertEqual(0, s.findMin(nums[i:] + nums[:i]))


if __name__ == '__main__':
    unittest.main()
