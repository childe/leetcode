# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""


class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = list()
        n = len(nums)
        for i in nums:
            # print i,nums
            if nums[-abs(i)] > 0:
                nums[-abs(i)] *= -1
            else:
                result.append(abs(i))
        return result


def main():
    s = Solution()
    # print s.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1])
    print s.findDuplicates([1, 3, 2, 4, 8, 2, 3, 1])


if __name__ == '__main__':
    main()
