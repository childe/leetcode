#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/contains-duplicate-iii/description/

Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

Example 1:
Input: nums = [1,2,3,1], k = 3, t = 0
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1, t = 2
Output: true

Example 3:
Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false

'''


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        >>> s = Solution()
        >>> s.containsNearbyAlmostDuplicate(nums = [1,2,3,1], k = 3, t = 0)
        True
        >>> s.containsNearbyAlmostDuplicate(nums = [1,0,1,1], k = 1, t = 2)
        True
        >>> s.containsNearbyAlmostDuplicate(nums = [1,5,9,1,5,9], k = 2, t = 3)
        False
        >>> s.containsNearbyAlmostDuplicate(nums = [2,2], k = 3, t = 0)
        True
        >>> s.containsNearbyAlmostDuplicate([7,1,3], 2, 3)
        True
        """
        import math
        k = min(k, len(nums)-1)
        for i, n in enumerate(nums):
            for nn in nums[i+1:i+k+1]:
                if math.fabs(nn - n) <= t:
                    return True
        return False
