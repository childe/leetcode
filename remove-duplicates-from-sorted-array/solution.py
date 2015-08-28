#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.
"""

import unittest


class Solution(object):

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0

        n = len(nums)
        idx1 = idx2 = 0
        while idx2<n:
            while nums[idx1] == nums[idx2]:
                idx2 += 1
                if idx2>=n:
                    return idx1+1
            idx1 += 1
            nums[idx1] = nums[idx2]
        return idx1+1


class TestSolution(unittest.TestCase):

    def test_removeDuplicates(self):
        s = Solution()

        l = []
        setl = set(l)
        s.removeDuplicates(l)
        self.assertEqual(len(set(l)), s.removeDuplicates(l))
        self.assertEqual(setl, set(l))

        l = [1,2,2,3,3,3]
        self.assertEqual(len(set(l)), s.removeDuplicates(l))

        import random
        for i in range(100):
            l = []
            for j in range(random.randint(1, 1000)):
                l.append(random.randint(1, 100))
            l.sort()

            self.assertEqual(len(set(l)), s.removeDuplicates(l))
            setl = set(l)
            s.removeDuplicates(l)
            self.assertEqual(setl, set(l))


if __name__ == '__main__':
    unittest.main()
