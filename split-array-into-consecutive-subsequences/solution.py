# -*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/split-array-into-consecutive-subsequences/

659. Split Array into Consecutive Subsequences
You are given an integer array nums that is sorted in non-decreasing order.

Determine if it is possible to split nums into one or more subsequences such that both of the following conditions are true:

Each subsequence is a consecutive increasing sequence (i.e. each integer is exactly one more than the previous integer).
All subsequences have a length of 3 or more.
Return true if you can split nums according to the above conditions, or false otherwise.

A subsequence of an array is a new array that is formed from the original array by deleting some (can be none) of the elements without disturbing the relative positions of the remaining elements. (i.e., [1,3,5] is a subsequence of [1,2,3,4,5] while [1,3,2] is not).

 

Example 1:

Input: nums = [1,2,3,3,4,5]
Output: true
Explanation: nums can be split into the following subsequences:
[1,2,3,3,4,5] --> 1, 2, 3
[1,2,3,3,4,5] --> 3, 4, 5

Example 2:

Input: nums = [1,2,3,3,4,4,5,5]
Output: true
Explanation: nums can be split into the following subsequences:
[1,2,3,3,4,4,5,5] --> 1, 2, 3, 4, 5
[1,2,3,3,4,4,5,5] --> 3, 4, 5

Example 3:

Input: nums = [1,2,3,4,4,5]
Output: false
Explanation: It is impossible to split nums into consecutive increasing subsequences of length 3 or more.
 

Constraints:

1 <= nums.length <= 10^4
-1000 <= nums[i] <= 1000
nums is sorted in non-decreasing order.

通过次数28,955提交次数53,456
"""


class Solution:
    def findStarsPoints(self, nums: list[int]) -> list[int]:
        """
        >>> s = Solution()
        >>> s.findStarsPoints([1,2,4,5])
        [1, 4]
        >>> s.findStarsPoints([1,1,1,2,2,3])
        [1, 1, 1]
        >>> s.findStarsPoints([1,2,3])
        [1]
        >>> s.findStarsPoints([1,2,3,4,4,5])
        [1, 4]
        >>> s.findStarsPoints([1,2,3,3,4,5])
        [1, 3]
        >>> s.findStarsPoints([1,2,3,3,4,4,5,5])
        [1, 3]
        """
        rst = []

        counter = dict([(n, int(0)) for n in range(nums[0] - 1, nums[-1] + 2)])
        for n in nums:
            counter[n] += 1

        for i in range(nums[0], nums[-1] + 1):
            rst.extend([i] * (counter[i] - counter[i - 1]))

        return rst

    def findEndsPoints(self, nums: list[int]) -> list[int]:
        """
        >>> s = Solution()
        >>> s.findEndsPoints([1,2,4,5])
        [2, 5]
        >>> s.findEndsPoints([1,2,2,3,3,3])
        [3, 3, 3]
        >>> s.findEndsPoints([1,2,2,2,2,3,3,3])
        [2, 3, 3, 3]
        >>> s.findEndsPoints([1,2,3])
        [3]
        >>> s.findEndsPoints([1,2,3,4,4,5])
        [4, 5]
        >>> s.findEndsPoints([1,2,3,3,4,5])
        [3, 5]
        >>> s.findEndsPoints([1,2,3,3,4,4,5,5])
        [5, 5]
        """
        rst = []

        counter = dict([(n, int(0)) for n in range(nums[0] - 1, nums[-1] + 2)])
        for n in nums:
            counter[n] += 1

        for i in range(nums[0], nums[-1] + 1):
            rst.extend([i] * (counter[i] - counter[i + 1]))

        return rst

    def isPossible(self, nums: list[int]) -> bool:
        """
        >>> s = Solution()
        >>> s.isPossible([1,2,3,4,4,5])
        False
        >>> s.isPossible([1,2,3,3,4,4,5,5])
        True
        >>> s.isPossible([1,2,3,3,4,5])
        True
        >>> s.isPossible([1,2,3,4,6,7,8,9,10,11])
        True
        """

        startsPoint, endPoints = self.findStarsPoints(nums), self.findEndsPoints(nums)

        for sn in startsPoint:
            for en in endPoints:
                if en - sn >= 2:
                    endPoints.remove(en)
                    break
            else:
                return False

        return True
