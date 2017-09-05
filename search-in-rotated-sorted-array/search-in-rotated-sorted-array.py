#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/search-in-rotated-sorted-array/

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
"""


class Solution(object):
    def find_demarcation(self, nums):
        """
        rtype: int
        >>> s = Solution()
        >>> s.find_demarcation([1])
        0
        >>> s.find_demarcation([1,2,3,4])
        0
        >>> s.find_demarcation([5,1,2,3,4])
        1
        >>> s.find_demarcation([3,4,1,2])
        2
        >>> s.find_demarcation([3,4,0,1,2])
        2
        >>> s.find_demarcation([3,4,5,2])
        3
        >>> s.find_demarcation([3,4,5,0,1,2])
        3
        """
        if nums[0] <= nums[-1]:
            return 0

        start, end = 0,  len(nums)-1
        while start < end:
            mid = (start+end)/2
            if nums[mid] >= nums[0]:
                start = mid+1
            else:
                end = mid
        return start

    def binary_search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        >>> s = Solution()
        >>> s.binary_search([1,2,3,4], 5)
        -1
        >>> s.binary_search([1], 1)
        0
        >>> s.binary_search([1,2,3,4], 1)
        0
        """
        start, end = 0,  len(nums)-1
        while start <= end:
            mid = (start+end)/2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                end = mid-1
            else:
                start = mid+1
        return -1

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        >>> s = Solution()
        >>> s.search([1,2,3,4], 5)
        -1
        >>> s.search([1], 1)
        0
        >>> s.search([1,2,3,4], 1)
        0
        >>> s.search([3,4,1,2], 1)
        2
        """
        if not nums:
            return -1

        demarcation = self.find_demarcation(nums)
        r1 = self.binary_search(nums[:demarcation], target)
        if r1 != -1:
            return r1
        r2 = self.binary_search(nums[demarcation:], target)
        if r2 == -1:
            return -1
        return demarcation + r2
