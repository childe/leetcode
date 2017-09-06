#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/search-for-a-range/description/

Given an array of integers sorted in ascending order, find the starting
and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        >>> s = Solution()
        >>> s.searchRange([1], 0)
        [-1, -1]
        >>> s.searchRange([1,2,3,4,6,6], 5)
        [-1, -1]
        >>> s.searchRange([1, 2, 3], 2)
        [1, 1]
        >>> s.searchRange([8, 8], 8)
        [0, 1]
        >>> s.searchRange([5, 7, 7, 8, 8, 10], 8)
        [3, 4]
        """
        if not nums:
            return [-1, -1]

        rst = []

        start, end = 0, len(nums)-1
        while start < end:
            mid = (start+end)/2
            if nums[mid] < target:
                start = mid+1
            elif nums[mid] > target:
                end = mid-1
            else:
                end = mid
        rst.append(start if nums[start] == target else -1)

        end = len(nums)-1
        while start < end:
            mid = (start+end+1)/2
            if nums[mid] < target:
                start = mid+1
            elif nums[mid] > target:
                end = mid-1
            else:
                start = mid
        rst.append(end if nums[end] == target else -1)

        return rst


if __name__ == '__main__':
    s = Solution()
    print s.searchRange([1, 2, 3], 2)
