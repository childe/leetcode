#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/remove-element/

Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
    Given input array nums = [3,2,2,3], val = 3

    Your function should return length = 2, with the first two elements of nums being 2.

Hint:

Try two pointers.
Did you use the property of "the order of elements can be changed"?
What happens when the elements to remove are rare?
"""

import unittest


class Solution(object):

    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        holder_idx = 0
        current_idx = 0
        for i,e in enumerate(nums):
            if e != val:
                if holder_idx!=current_idx:
                    nums[holder_idx] = e
                holder_idx += 1
            current_idx += 1

        return holder_idx


class testSolution(unittest.TestCase):

    def test_removeElement(self):
        s = Solution()
        nums = []
        my_rst = s.removeElement(nums, 0)
        self.assertEqual(my_rst, 0)
        self.assertEqual(nums, [])

        nums = [1,2]
        my_rst = s.removeElement(nums, 0)
        self.assertEqual(my_rst, 2)
        self.assertEqual(sorted(nums[:my_rst]), [1,2])

        nums = [1,2,2]
        my_rst = s.removeElement(nums, 2)
        self.assertEqual(my_rst, 1)
        self.assertEqual(sorted(nums[:my_rst]), [1])

        import random
        for i in range(1000):
            nums = [random.randint(1,10) for i in range(random.randint(0,10))]
            copy = nums[:]
            val = random.randint(0,11)
            my_rst = s.removeElement(nums, val)
            rst = []
            for e in copy:
                if e != val:
                    rst.append(e)
            self.assertEqual(my_rst, len(rst))
            self.assertEqual(sorted(nums[:my_rst]), sorted(rst))


if __name__ == '__main__':
    unittest.main()
