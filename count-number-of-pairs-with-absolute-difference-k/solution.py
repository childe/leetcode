#!
# -*- coding: utf-8 -*-

"""
2006. Count Number of Pairs With Absolute Difference K
Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.

The value of |x| is defined as:

x if x >= 0.
-x if x < 0.
 

Example 1:

Input: nums = [1,2,2,1], k = 1
Output: 4
Explanation: The pairs with an absolute difference of 1 are:

Example 2:

Input: nums = [1,3], k = 3
Output: 0
Explanation: There are no pairs with an absolute difference of 3.

Example 3:

Input: nums = [3,2,1,5,4], k = 2
Output: 3
Explanation: The pairs with an absolute difference of 2 are:


Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100
1 <= k <= 99
"""

from collections import Counter


class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        """
        >>> s = Solution()
        >>> s.countKDifference([1,2,2,1], 1)
        4
        >>> s.countKDifference([1,3], 3)
        0
        >>> s.countKDifference([3,2,1,5,4], 2)
        3
        """
        c = Counter(nums)
        nums = sorted(set(nums))
        i, j, l = 0, 0, len(c)
        ans = 0
        while j < l:
            # print(i, j, l, ans)
            diff = nums[j] - nums[i]
            # print(diff)
            if diff < k:
                j += 1
            elif diff == k:
                ans += c[nums[i]] * c[nums[j]]
                j += 1
                i += 1
            else:
                i += 1

        return ans
