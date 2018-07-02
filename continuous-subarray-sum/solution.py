#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/continuous-subarray-sum/description/

Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to the multiple of k, that is, sums up to n*k where n is also an integer.

Example 1:
Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
Example 2:
Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
Note:
The length of the array won't exceed 10,000.
You may assume the sum of all the numbers is in the range of a signed 32-bit integer.
"""


class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        >>> s = Solution()
        >>> s.checkSubarraySum([23, 2, 4, 6, 7],  k=6)
        True
        >>> s.checkSubarraySum([23, 2, 6, 4, 7],  k=6)
        True
        >>> s.checkSubarraySum([23, 2, 6, 4, 7],  k=0)
        False
        >>> s.checkSubarraySum([0, 0],  k=0)
        True
        >>> s.checkSubarraySum([0],  k=0)
        False
        >>> s.checkSubarraySum([1,2,3],  k=6)
        True
        >>> s.checkSubarraySum([0, 0],  k=-1)
        True
        """
        if not nums:
            return False

        # if '0,0' in nums
        flag = False
        for n in nums:
            if n != 0:
                flag = False
                continue
            if flag:
                return True
            flag = True

        if k == 0:
            return False

        if k < 0:
            k = -k

        if k > sum(nums):
            return False

        r = [set() for n in nums]
        r[0].add(nums[0] % k)
        for i, n in enumerate(nums):
            if i == 0:
                continue
            for e in r[i-1]:
                r[i].add((n+e) % k)
            if 0 in r[i]:
                return True
            r[i].add(n % k)
        return False
