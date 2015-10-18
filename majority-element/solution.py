#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
"""
https://leetcode.com/problems/majority-element/

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
"""


class Solution(object):

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx = 0
        length = len(nums)

        nums.append(nums.pop(0))
        while idx < length:
            if nums[idx] == nums[-1]:
                nums.append(nums[idx])
            else:
                nums.pop()
            idx += 1
        return nums[-1]


class TestSolution(unittest.TestCase):

    def test_majorityElement(self):
        from collections import Counter
        s = Solution()

        nums = [1]
        answer = Counter(nums).most_common()[0][0]
        myanswer = s.majorityElement(nums)
        self.assertEqual(answer, myanswer)

        nums = [1, 2, 1, 2, 1]
        answer = Counter(nums).most_common()[0][0]
        myanswer = s.majorityElement(nums)
        self.assertEqual(answer, myanswer)

        nums = [1, 1, 2, 2, 3, 3, 3, 3, 3]
        answer = Counter(nums).most_common()[0][0]
        myanswer = s.majorityElement(nums)
        self.assertEqual(answer, myanswer)

        nums = [1]*1000 + [2]*1001
        answer = Counter(nums).most_common()[0][0]
        myanswer = s.majorityElement(nums)
        self.assertEqual(answer, myanswer)

        import random

        for k in range(1000):
            nums = [
                random.randint(
                    1,
                    100) for i in range(
                    random.randint(
                        1,
                        100))]
            nums.extend([random.randint(1, 100)]*(len(nums)+1))
            answer = Counter(nums).most_common()[0][0]
            myanswer = s.majorityElement(nums)
            self.assertEqual(answer, myanswer)

            nums = [
                random.randint(
                    1,
                    100) for i in range(
                    random.randint(
                        1,
                        100))]
            nums.extend([101]*(len(nums)+1))
            answer = Counter(nums).most_common()[0][0]
            myanswer = s.majorityElement(nums)
            self.assertEqual(answer, myanswer)

if __name__ == '__main__':
    unittest.main()
