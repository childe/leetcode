#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/single-element-in-a-sorted-array/

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

 

Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10
 

Constraints:

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^5
通过次数67,754提交次数111,540
"""


class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        """
        >>> s = Solution()
        >>> s.singleNonDuplicate([1,1,2,3,3,4,4,8,8])
        2
        >>> s.singleNonDuplicate([3,3,7,7,10,11,11])
        10
        """
