#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}

    def twoSum(self, nums, target):
        d = {}
        for idx, e in enumerate(nums):
            if e in d:
                return d[e], idx+1
            d[target-e] = idx+1


class TestSolution(unittest.TestCase):

    def test_twoSum_random(self):
        import random
        s = Solution()

        for n in range(100):
            # test n times
            nums = list()
            for i in range(random.randint(2, 100)):
                nums.append(random.randint(1, 10000))

            nums = list(nums)
            i = nums[random.randint(0, len(nums)-1)]
            j = i
            while (j == i):
                j = nums[random.randint(0, len(nums))-1]
            target = i + j

            rst = s.twoSum(nums, target)
            self.assertTrue(rst[0] < rst[1])
            self.assertEqual(target, nums[rst[0]-1]+nums[rst[1]-1])

    def test_twoSum_same(self):
        """nums has same element , and target is the sum of them two"""
        import random
        s = Solution()

        for n in range(100):
            # test n times
            nums = list()
            for i in range(random.randint(2, 100)):
                nums.append(random.randint(1, 10000))
            the_one = random.randint(1, 10000)
            nums.append(the_one)
            nums.append(the_one)
            random.shuffle(nums)

            target = the_one * 2

            rst = s.twoSum(nums, target)
            self.assertTrue(rst[0] < rst[1])
            self.assertEqual(target, nums[rst[0]-1]+nums[rst[1]-1])

if __name__ == '__main__':
    unittest.main()
