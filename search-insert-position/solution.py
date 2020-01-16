# -*- coding: utf-8 -*-

'''
https://leetcode-cn.com/problems/search-insert-position/

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.


Example 1:
Input: [1,3,5,6], 5
Output: 2


Example 2:
Input: [1,3,5,6], 2
Output: 1


Example 3:
Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
'''


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        s, e = 0, len(nums)-1
        while s <= e:
            m = (s+e)//2
            if target == nums[m]:
                return m
            if target < nums[m]:
                e = m-1
            else:
                s = m+1
        return s


def main():
    s = Solution()
    nums = [1, 3, 5, 6]
    target = 5
    a = 2
    assert s.searchInsert(nums, target) == a

    nums = [1, 3, 5, 6]
    target = 2
    a = 1
    assert s.searchInsert(nums, target) == a

    nums = [1, 3, 5, 6]
    target = 7
    a = 4
    assert s.searchInsert(nums, target) == a

    nums = [1, 3, 5, 6]
    target = 0
    a = 0
    assert s.searchInsert(nums, target) == a


if __name__ == '__main__':
    main()
