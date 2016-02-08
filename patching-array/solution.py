#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/patching-array/

Given a sorted positive integer array nums and an integer n, add/patch elements to the array such that any number in range [1, n] inclusive can be formed by the sum of some elements in the array. Return the minimum number of patches required.

Example 1:
nums = [1, 3], n = 6
Return 1.

Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
So we only need 1 patch.

Example 2:
nums = [1, 5, 10], n = 20
Return 2.
The two patches can be [2, 4].

Example 3:
nums = [1, 2, 2], n = 5
Return 0.
Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.

Subscribe to see which companies asked this question

Show Tags
"""

import unittest

class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        count = 0
        p1 = 0
        p2 = 1
        added = []
        while(p2<=n):
            if nums[p1:] and nums[p1] <= p2:
                p2 += nums[p1]
                p1 += 1
            else:
                count += 1
                added.append(p2)
                p2 += p2

        return count



class TestSolution(unittest.TestCase):
    def test_minPatches(self):
        s = Solution()
        my_answer = s.minPatches([1,3],6)
        self.assertEqual(my_answer, 1)

        my_answer = s.minPatches([1,5,10],20)
        self.assertEqual(my_answer, 2)

        my_answer = s.minPatches([1,2,2],5)
        self.assertEqual(my_answer, 0)

        my_answer = s.minPatches([],5)
        self.assertEqual(my_answer, 3)

        my_answer = s.minPatches([],10)
        self.assertEqual(my_answer, 4)

        my_answer = s.minPatches([1],10)
        self.assertEqual(my_answer, 3)



if __name__ == '__main__':
    unittest.main()
