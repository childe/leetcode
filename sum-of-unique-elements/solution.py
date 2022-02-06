#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/sum-of-unique-elements/

1748. Sum of Unique Elements
You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.

Return the sum of all the unique elements of nums.

 

Example 1:
Input: nums = [1,2,3,2]
Output: 4
Explanation: The unique elements are [1,3], and the sum is 4.

Example 2:
Input: nums = [1,1,1,1,1]
Output: 0
Explanation: There are no unique elements, and the sum is 0.

Example 3:
Input: nums = [1,2,3,4,5]
Output: 15
Explanation: The unique elements are [1,2,3,4,5], and the sum is 15.
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
"""


class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        """
        >>> s = Solution()
        >>> s.sumOfUnique([1,2,3,2])
        4
        >>> s.sumOfUnique([1,1,1,1,1])
        0
        >>> s.sumOfUnique([1,2,3,4,5])
        15
        """
        arr = [0] * 101
        for n in nums:
            arr[n] += 1

        ans = 0
        for i, n in enumerate(arr):
            if n == 1:
                ans += i

        return ans
