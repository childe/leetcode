# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/wiggle-sort-ii/description/

Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

Example 1:

Input: nums = [1, 5, 1, 1, 6, 4]
Output: One possible answer is [1, 4, 1, 5, 1, 6].
Example 2:

Input: nums = [1, 3, 2, 2, 3, 1]
Output: One possible answer is [2, 3, 1, 3, 1, 2].
Note:
You may assume all input has valid answer.

Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?
"""


class Solution(object):
    def sort(self, nums, medium):
        """
        >>> s = Solution()
        >>> nums = [4, 5, 5, 6]
        >>> s.sort(nums, 5)
        (1, 2)
        >>> nums
        [4, 5, 5, 6]
        >>> nums = [4, 5, 6, 5]
        >>> s.sort(nums, 5)
        (1, 2)
        >>> nums
        [4, 5, 5, 6]
        >>> nums =[3, 2, 4, 1, 5]
        >>> s.sort(nums, 3)
        (2, 2)
        >>> nums
        [2, 1, 3, 4, 5]
        """
        p = None  # point to first num >= medium
        for i, n in enumerate(nums):
            if n >= medium:
                if p is None:
                    p = i
            else:
                if p is not None:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1

        j, p = p, None  # point to first num > medium
        for i in range(j, len(nums)):
            if nums[i] > medium:
                if p is None:
                    p = i
            else:
                if p is not None:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
        if p is None:
            return j, len(nums) - 1
        return j, p-1

    def findKMedium(self, nums, k):
        # print '~~', nums, k
        if k >= len(nums):
            return nums[-1]
        if len(nums) <= 5:
            nums.sort()
            return nums[k]

        # find medium of mediums
        l = len(nums)
        mediums = []
        for i in range(0, l - l % 5, 5):
            mediums.append(sorted(nums[i:i+4])[2])
        if l % 5 != 0:
            ns = sorted(nums[i+5:l])
            mediums.append(ns[len(ns)//2])
        medium = self.findKMedium(mediums, len(mediums)//2)
        # print 'mediums', mediums, medium

        # sort based on MOfM
        low, high = self.sort(nums, medium)
        # print nums, low, high

        if low <= k <= high:
            return medium
        if low > k:
            return self.findKMedium(nums[:low], k)
        return self.findKMedium(nums[high+1:], k-high-1)

    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        >>> import random
        >>> s = Solution()
        >>> nums = range(10)
        >>> random.shuffle(nums)
        >>> s.wiggleSort(nums)
        >>> all([n < nums[i+1] if i % 2 == 0 else n > nums[i+1] for i, n in enumerate(nums[:-1])])
        True
        >>> nums = range(100)
        >>> random.shuffle(nums)
        >>> s.wiggleSort(nums)
        >>> all([n < nums[i+1] if i % 2 == 0 else n > nums[i+1] for i, n in enumerate(nums[:-1])])
        True
        >>> nums = [1,2,2,1,2,1,1,1,1,2,2,2]
        >>> s.wiggleSort(nums)
        >>> all([n < nums[i+1] if i % 2 == 0 else n > nums[i+1] for i, n in enumerate(nums[:-1])])
        True
        >>> nums = [4,5,5,6]
        >>> s.wiggleSort(nums)
        >>> all([n < nums[i+1] if i % 2 == 0 else n > nums[i+1] for i, n in enumerate(nums[:-1])])
        True
        """
        medium = self.findKMedium(nums, len(nums)//2)
        self.sort(nums, medium)
        m = (len(nums) - 1) // 2
        nums[::2], nums[1::2] = nums[m::-1], nums[-1:m:-1]


def main():
    import random
    s = Solution()
    nums = [1, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1, 2, 1, 2, 1, 1, 2]
    # print s.findKMedium(nums, len(nums) // 2)
    # print nums
    # return

    nums = [1,5,1,1,6,4]

    s.wiggleSort(nums)
    print nums

    print all([n < nums[i+1] if i % 2 == 0 else n > nums[i+1] for i, n in enumerate(nums[:-1])])


if __name__ == '__main__':
    main()
