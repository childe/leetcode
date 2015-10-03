#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
"""
https://leetcode.com/problems/3sum-closest/


Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""


class Solution(object):

    def _threeSumClosest(self, nums, n, target):
        """
        :type nums: List[int]
        :type n: int
        :type target: int
        :rtype: int
        """
        # print nums,n,target
        if nums[n:] == []:
            return sum(nums)
        if n == 1:
            closest = nums[0]
            closest_diff = abs(closest - target)
            for num in nums[1:]:
                if abs(num-target) < closest_diff:
                    closest_diff = abs(num-target)
                    closest = num
                else:
                    return closest
            return closest

        closest = []
        for idx, num in enumerate(nums):
            if idx > 0 and num == nums[idx-1]:
                continue
            closest.append(
                num +
                self._threeSumClosest(
                    nums[
                        :idx] +
                    nums[
                        idx +
                        1:],
                    n -
                    1,
                    target -
                    num))
        # print nums,n,target,"closest: ",closest
        closest_diff = abs(closest[0]-target)
        rst = closest[0]
        for c in closest[1:]:
            if abs(c-target) < closest_diff:
                closest_diff = abs(c-target)
                rst = c
        return rst

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()

        length = len(nums)

        candidates = set()

        for idx, num in enumerate(nums):
            nums_without_num = nums[:idx]+nums[idx+1:]

            new_target = target-num
            i = 0
            j = length-2

            while(i < j):
                s = nums_without_num[i]+nums_without_num[j]
                if s == new_target:
                    return target
                candidates.add(num+s)
                if s < new_target:
                    i += 1
                else:
                    j -= 1

        closest = candidates.pop()
        for c in candidates:
            if abs(c-target) < abs(closest-target):
                closest = c

        return closest


class TestSolution(unittest.TestCase):

    def test__threeSumClosest(self):
        s = Solution()
        nums = [2, 3, 4]
        n = 2
        target = 5
        self.assertEqual(5, s._threeSumClosest(nums, n, target))

    def test_threeSumClosest(self):
        s = Solution()
        import random
        nums = [random.randint(-10000, 10000)
                for e in range(100)]
        self.assertEqual(0, s.threeSumClosest(nums, 0))

        nums = [random.randint(-10000, 10000)
                for e in range(1000)]
        self.assertEqual(0, s.threeSumClosest(nums, 0))

        nums = [1, 2, 3, 4]
        target = 6
        self.assertEqual(6, s.threeSumClosest(nums, target))

        nums = [0, 0, 0]
        target = 1
        self.assertEqual(0, s.threeSumClosest(nums, target))

        nums = [38, 60, -
                3, -
                12, 48, 100, 18, -
                76, -
                12, -
                99, 45, 67, 42, 66, -
                25, -
                38, -
                52, -
                53, 57, 53, 100, -
                60, 75, -
                75, -
                52, -
                98, 80, 49, 87, 35, 9, 6, -
                37, 48, 23, -
                30, 86, -
                6, 57, 80, 86, 39, -
                74, -
                18, 0, 37, -
                93, -
                36, 1, 89, -
                51, -
                80, -
                40, -
                63, -
                32, 4, -
                52, 48, 29, -
                52, -
                86, 4, -
                32, -
                73, 91, 91, 11, 44, 22, 47, 48, 38, 61, -
                92, -
                86, 86, 98, 15, -
                97, 96, -
                82, 94, -
                22, 77, -
                44, -
                66, -
                40, -
                58, -
                89, 23, -
                24, -
                11, -
                64, -
                17, 12, 12, -
                30, 19, 43, 64, -
                85, -
                44, -
                65, -
                58, 83, -
                94, 55, 95, 63, 11, 56, -
                35, -
                62, -
                38, 15, -
                91, -
                97, -
                57, 69, -
                82, -
                61, 58, -
                12, 32, -
                96, -
                16, -
                33, 37, -
                72, -
                66, 43, 19, 23, -
                33, -
                22, -
                44, -
                22, 97, 87, -
                75, 38, 100, 9, 99, 10, 0, -
                86, -
                25, 95, -
                1, 39, 32, 45, -
                61, 24, 80, -
                59, 66, -
                81, -
                82, 27, -
                77, 34, -
                88, 25, 12, 66, 57, 39, -
                75, 86, 92, -
                65, -
                12, -
                87, 2, -
                7, -
                58, -
                46, -
                3, -
                67, 1, -
                92, -
                77, -
                42, 60, 72, 71, 74, -
                82, 75, -
                39, 28, 91, -
                76, -
                10, -
                41, -
                41, 36, 63, -
                35, 71, -
                6, -
                8, -
                57, 6, -
                5, 80, 76, -
                73, 96, -
                59, 61, -
                69, 84, -
                40, -
                87]
        target = -20
        self.assertEqual(-20, s.threeSumClosest(nums, target))

        nums = [-3, -26, 43, 51, -70, -17, 31, 23]
        target = 289
        self.assertEqual(125, s.threeSumClosest(nums, target))

        import random
        import itertools
        nums = [random.randint(-100, 100)
                for e in range(random.randint(3, 10))]
        target = random.randint(0, 300)
        my_answer = s.threeSumClosest(nums, target)
        for e in itertools.combinations(nums, 3):
            self.assertTrue(abs(my_answer-target) <= abs(sum(e)-target))


if __name__ == '__main__':
    unittest.main()
