# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/find-the-duplicate-number/description/


Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""


class Solution(object):
    def findNumCountsBasedonMid(self, nums, low, high, mid1, mid2):
        a, b = 0, 0
        for n in nums:
            if low <= n <= mid1:
                a += 1
            if mid2 <= n <= high:
                b += 1
        return a, b

    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        >>> s = Solution()
        >>> s.findDuplicate([1,3,4,2,2])
        2
        >>> s.findDuplicate([3,1,3,4,2])
        3
        """
        low, high = 1, len(nums)
        mid1, mid2 = (low+high)/2, (low+high+1)/2
        while low < high:
            # print low, high, mid1, mid2
            a, b = self.findNumCountsBasedonMid(nums, low, high, mid1, mid2)
            # print a, b
            if a == b:
                return mid1
            if a > b:
                high = mid1
            else:
                low = mid2
            mid1, mid2 = (low+high)/2, (low+high+1)/2
        return low


if __name__ == '__main__':
    s = Solution()
    # print s.findDuplicate([2, 3, 4, 2, 2])
    print s.findDuplicate([3,1,3,4,2])
