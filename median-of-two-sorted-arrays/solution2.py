#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/median-of-two-sorted-arrays/
There are two sorted arrays nums1 and nums2 of size m and n respectively. Find the median of the two
sorted arrays. The overall run time complexity should be O(log (m+n)).
"""

import unittest


class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}

    def findMedianSortedArrays(self, nums1, nums2):
        #print nums1, nums2
        if not nums2:
            return 1.0*(nums1[(len(nums1)-1)/2]+nums1[len(nums1)/2])/2
        if not nums1:
            return 1.0*(nums2[(len(nums2)-1)/2]+nums2[len(nums2)/2])/2

        offset = 0

        c = 0
        while nums1 and nums2:
            #print
            #print nums1, nums2, offset
            n1 = len(nums1)
            n2 = len(nums2)
            n = n1+n2
            if n <= 2:
                break

            c = (c+1)%2
            #print "c",c
            idx1 = (n1-c)/2
            idx2 = (n2-c)/2
            n += abs(offset)
            #print "n", n

            mid1 = nums1[idx1]
            mid2 = nums2[idx2]
            #print "mid1,mid2",mid1,mid2

            # +n, 左移n个, 0不变, -n将m1自身移除
            small_carry = max(-1, n/2-n1-n2+idx1+idx2+1-max(0, offset))

            # +n,需要右移n个, 如果0,不变, -n,移除m2本身
            big_carry = max(-1, n/2-idx1-idx2-1+min(0, offset))
            #print "small_carry", small_carry
            #print "big_carry", big_carry

            small_nums, big_nums = (
                nums1, nums2) if mid1 < mid2 else (
                nums2, nums1)
            small_idx, big_idx = (idx1,idx2) if  mid1 < mid2 else (idx2,idx1)

            left = small_idx - small_carry
            left = max(0, left)
            #print "left", left
            nums1 = small_nums[left:]

            right = big_idx + 1 + big_carry
            #print "right", right
            nums2 = big_nums[:right]

            offset = len(big_nums)-len(nums2) - \
                (len(small_nums)-len(nums1)) + offset

        #print nums1, nums2, offset
        nums = sorted(nums1+nums2)
        if offset < 0:
            nums = [0]*(-offset)+nums
        elif offset > 0:
            nums = nums+[0]*offset

        return 1.0*(nums[(len(nums)-1)/2]+nums[len(nums)/2])/2


class TestSolution(unittest.TestCase):

    def test_findMedianSortedArrays(self):
        import random
        s = Solution()

        nums1 = [2, 15, 28, 38, 43, 51, 56, 90, 93, 93]
        nums2 = [2, 5, 6, 12, 34, 54, 56, 74, 98]
        rst = s.findMedianSortedArrays(nums1, nums2)
        nums = sorted(nums1+nums2)
        rst2 = 1.0*(nums[(len(nums)-1)/2]+nums[len(nums)/2])/2
        self.assertEqual(rst, rst2)
        #return

        #nums1 = [1, 3, 5]
        #nums2 = [2, 4, 6]
        #rst = s.findMedianSortedArrays(nums1, nums2)
        #nums = sorted(nums1+nums2)
        #rst2 = 1.0*(nums[(len(nums)-1)/2]+nums[len(nums)/2])/2
        #self.assertEqual(rst, rst2)

        #nums1 = [1, 3, 5, 7]
        #nums2 = [2, 4, 6, 8]
        #rst = s.findMedianSortedArrays(nums1, nums2)
        #nums = sorted(nums1+nums2)
        #rst2 = 1.0*(nums[(len(nums)-1)/2]+nums[len(nums)/2])/2
        #self.assertEqual(rst, rst2)

        for i in range(10000):
            nums1 = []
            nums2 = []
            for i in range(random.randint(1, 10)):
                nums1.append(random.randint(0, 100))
            for i in range(random.randint(1, 10)):
                nums2.append(random.randint(0, 100))
            nums1.sort()
            nums2.sort()
            rst = s.findMedianSortedArrays(nums1, nums2)
            nums = sorted(nums1+nums2)
            rst2 = 1.0*(nums[(len(nums)-1)/2]+nums[len(nums)/2])/2
            # print rst, rst2
            self.assertEqual(rst, rst2)

if __name__ == '__main__':
    unittest.main()
