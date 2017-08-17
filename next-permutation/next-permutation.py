# -*- coding: utf-8 -*-

import unittest

'''
https://leetcode.com/problems/next-permutation/description/

Implement next permutation, which rearranges numbers into the lexicographically
next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible
order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding
outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''


class Solution(object):
    def _isMaxPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 1:
            return True
        return nums[0] >= nums[1]

    def _reverse(self, nums, idx):
        """
        :type nums: List[int]
        :type idx: int
        >>> s = Solution()
        >>> nums = [1, 5, 4, 3, 2]
        >>> s._reverse(nums, 1)
        >>> nums
        [1, 2, 3, 4, 5]
        """
        i, j = idx, len(nums)-1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    def _partNextPermutation(self, nums, idx):
        """
        :type nums: List[int]
        :type idx: int
        >>> s = Solution()
        >>> nums = [1, 3, 2]
        >>> s._partNextPermutation(nums, 0)
        >>> nums
        [2, 1, 3]
        >>> nums = [1, 3, 2]
        >>> s._partNextPermutation(nums, -3)
        >>> nums
        [2, 1, 3]
        >>> nums = [1, 3, 1, 6, 5, 2]
        >>> s._partNextPermutation(nums, -4)
        >>> nums
        [1, 3, 2, 1, 5, 6]
        >>> nums = [1, 3, 1, 6, 5, 2]
        >>> s._partNextPermutation(nums, 2)
        >>> nums
        [1, 3, 2, 1, 5, 6]
        >>> nums = [4, 5, 4, 3, 2, 1]
        >>> s._partNextPermutation(nums, 0)
        >>> nums
        [5, 1, 2, 3, 4, 4]
        """
        idx = (len(nums) + idx) % len(nums)
        # assert(self._isMaxPermutation(nums[idx+1:]))
        t = nums[idx]
        for i in range(len(nums)-1, idx, -1):
            if nums[idx] < nums[i]:
                nums[i], nums[idx] = nums[idx], nums[i]
                self._reverse(nums, 1+idx)
                break
        # else:
            # raise

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(1, 1+len(nums)):
            if self._isMaxPermutation(nums[-i:]):
                continue
            else:
                return self._partNextPermutation(nums, -i)

        return nums.reverse()


class TestSolution(unittest.TestCase):

    def test_findMedianSortedArrays(self):
        s = Solution()

        nums = [1, 2, 3]
        s.nextPermutation(nums)
        self.assertEqual(nums, [1, 3, 2])

        nums = [3, 2, 1]
        s.nextPermutation(nums)
        self.assertEqual(nums, [1, 2, 3])

        nums = [1, 1, 5]
        s.nextPermutation(nums)
        self.assertEqual(nums, [1, 5, 1])

        nums = [1, 3, 2]
        s.nextPermutation(nums)
        self.assertEqual(nums, [2, 1, 3])

        nums = [1, 3, 4, 5, 6, 3, 1, 2, 4, 3, 5, 6, 7, 1, 1]
        s.nextPermutation(nums)
        self.assertEqual(nums, [1, 3, 4, 5, 6, 3, 1, 2, 4, 3, 5, 7, 1, 1, 6])


if __name__ == '__main__':
    unittest.main()
