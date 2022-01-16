#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/max-number-of-k-sum-pairs/

You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

 

Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.
 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
1 <= k <= 10^9
"""

from collections import Counter


class Solution:
    def maxOperations1(self, c: Counter, k: int) -> int:
        ans = 0
        for i in range(1, (1 + k) // 2):
            ans += min(c.get(i, 0), c.get(k - i, 0))

        if k % 2 == 0:
            ans += c.get(k // 2, 0) // 2
        return ans

    def maxOperations2(self, c: Counter, k: int) -> int:
        keys = c.keys()
        ans = 0
        for i in keys:
            ans += min(c.get(i, 0), c.get(k - i, 0))
        return ans // 2

    def maxOperations(self, nums: list[int], k: int) -> int:
        """
        >>> s = Solution()
        >>> s.maxOperations(nums = [1,2,3,4], k = 5)
        2
        >>> s = Solution()
        >>> s.maxOperations(nums = [3,1,3,4,3], k = 6)
        1
        """
        nums = [n for n in nums if n < k]
        c = Counter(nums)
        if len(c) > k:
            return self.maxOperations1(c, k)
        else:
            return self.maxOperations2(c, k)
