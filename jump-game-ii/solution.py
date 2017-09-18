#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/jump-game-ii/description/

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
    Given array A = [2,3,1,1,4]

    The minimum number of jumps to reach the last index is 2.
    (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

    Note:
        You can assume that you can always reach the last index.
"""


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        >>> s=Solution()
        >>> s.jump([2])
        0
        >>> s.jump([2,3,1,1,4])
        2
        >>> s.jump([1,2,3,4,5,6,7,8,9])
        4
        >>> s.jump([9,8,7,6,5,4,3,2,1])
        1
        >>> s.jump([1]*10)
        9
        >>> s.jump([1,2,3,4,2,2,3,1,3,4,6,7,2,1,3,3,1,3,1,2,3,6])
        8
        """
        stepList = [0] * len(nums)
        stepList[1:1+nums[0]] = [1] * (1+nums[0])
        lastLargetestPoint = 0
        for i, num in enumerate(nums[:-1]):
            # print i, num, nums[lastLargetestPoint], lastLargetestPoint
            if num <= nums[lastLargetestPoint] - (i-lastLargetestPoint):
                continue
            stepList[1+lastLargetestPoint+nums[lastLargetestPoint]:
                     1+i+num] = [1+stepList[i]] * (i+num-lastLargetestPoint-nums[lastLargetestPoint])
            lastLargetestPoint = i
            # print stepList

        return stepList[len(nums)-1]


if __name__ == '__main__':
    s = Solution()
    print s.jump([2, 3, 1, 1, 4])
