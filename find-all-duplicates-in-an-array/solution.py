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
        >>> s = Solution()
        >>> s.findDuplicates([4,3,2,7,8,2,3,1])
        [2, 3]
        """
        l = len(nums)
        rst = []
        for i in range(l):
            # print 'i', i, nums
            n = nums[i]
            if n == l+1:
                continue
            if n == i + 1:
                nums[i] = l+1
                continue
            nums[i] = 0
            while True:
                # print nums
                if nums[n-1] == l+1:
                    rst.append(n)
                    # print rst
                    break
                elif nums[n-1] == 0:
                    nums[n-1] = l+1
                    break
                nums[n-1], n = l+1, nums[n-1]

        return rst


def main():
    s = Solution()
    # print s.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1])
    print s.findDuplicates([1, 3, 2, 4, 8, 2, 3, 1])


if __name__ == '__main__':
    main()
