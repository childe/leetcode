#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}

    def twoSum(self, nums, target):
        soted_nums = sorted(nums)
        for idx_i, i in enumerate(soted_nums):
            for idx_j, j in enumerate(soted_nums[idx_i+1:]):
                if i+j == target:
                    rst1 = nums.index(i)+1
                    if j == i:
                        rst2 = nums[rst1:].index(j)+rst1+1
                    else:
                        rst2 = nums.index(j)+1
                    rst = sorted([rst1, rst2])
                    return rst
                elif i+j > target:
                    break


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
