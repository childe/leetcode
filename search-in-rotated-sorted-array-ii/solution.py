# -*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/

81. 搜索旋转排序数组 II

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
Follow up:

This is a follow up problem to [Search in Rotated Sorted Array](https://leetcode-cn.com/problems/search-in-rotated-sorted-array/description/), where nums may contain duplicates.
Would this affect the run-time complexity? How and why?
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        s, e = 0, len(nums) - 1
        while s <= e:
            m = (s + e + 1) // 2
            n = nums[m]
            # print(s, e, nums[s : e + 1], n)

            if n == target:
                return True

            if target == nums[s]:
                return True

            if n == nums[s]:
                s += 1
                continue

            if n > nums[s]:  # m 左边是单调的
                if target > n:
                    s = m + 1
                    continue
                if target < nums[s]:
                    s = m + 1
                else:
                    e = m - 1
            else:  # m 右边是单调的
                if target < n:
                    e = m - 1
                    continue
                if target < nums[s]:
                    s = m + 1
                else:
                    e = m - 1
        return False


def main():
    s = Solution()

    nums = [1, 1, 1, 3, 1]
    target = 3
    ans = s.search(nums, target)
    print(ans)
    assert ans is True

    nums = [1, 1]
    target = 2
    ans = s.search(nums, target)
    print(ans)
    assert ans is False

    nums = [1]
    target = 1
    ans = s.search(nums, target)
    print(ans)
    assert ans is True

    nums = [2, 5, 6, 0, 0, 1, 2]
    target = 0
    ans = s.search(nums, target)
    print(ans)
    assert ans is True

    nums = [2, 5, 6, 0, 0, 1, 2]
    target = 3
    ans = s.search(nums, target)
    print(ans)
    assert ans is False


if __name__ == "__main__":
    main()
