#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/median-of-two-sorted-arrays/
There are two sorted arrays nums1 and nums2 of size m and n respectively. Find the median of the two
sorted arrays. The overall run time complexity should be O(log (m+n)).

1. 每个列表取中间数字 nums[len(nums)/2], 记做x,y, 假设x<=y
2. median 应该在 numX[x.index:] 和 numY[:y.index+1] 之间
3. 因为去掉了一些数字, 假设numX中去掉了左边a个数字, numY中去掉了右边b个数字,记offset=a-b 后续操作需要向左扩展offset个数字. (如果offset<0, 就是向右扩展)
4. 对新的留下来的数据, 重复1,2步骤. 但是因为3, 需要做扩展, 并且每次重复1,2之后, 要更新offset值
5. 总长度小于XXXX时, 可以直接合并.

在实际操作中, 不会`去掉左边数据, 保留右边数据`, 而是通过index标识当前的位置.

"""

import unittest


class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}

    def findMedianSortedArrays(self, nums1, nums2):
        offset = 0
        # loop_index = 1
        startX, startY, endX, endY = 0, 0, len(nums1), len(nums2)
        while endX-startX + endY-startY > 50:
            #print 'loop_index', loop_index
            # loop_index += 1

            # nums = sorted(nums1[startX:endX]+nums2[startY:endY])
            # r = (nums[(len(nums)-1-offset)/2]+nums[(len(nums)-offset)/2])/2.0
            #print offset, startX, endX, startY, endY, nums1[startX:endX], nums2[startY:endY], nums, r

            lenX, lenY = endX - startX, endY-startY
            midX = (endX-startX)/2+startX
            midY = (endY-startY)/2+startY

            #print nums1[midX], nums2[midY]

            if nums1[midX] <= nums2[midY]:
                original, startX = startX, midX-1
                startX = max(original, min(startX, startX-offset))

                original, endY = endY, midY+1
                endY = min(original, max(endY, endY-offset))

            else:
                original, endX = endX, midX+1
                endX = min(original, max(endX, endX-offset))

                original, startY = startY, midY-1
                startY = max(original, min(startY, startY-offset))

            offset = startX - (len(nums1) - endX) + startY - (len(nums2)-endY)

            #print

        nums = sorted(nums1[startX:endX]+nums2[startY:endY])
        r = (nums[(len(nums)-1-offset)/2]+nums[(len(nums)-offset)/2])/2.0
        #print offset, startX, endX, startY, endY, nums1[startX:endX], nums2[startY:endY], nums, r
        return r



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
            # #print rst, rst2
            self.assertEqual(rst, rst2)


if __name__ == '__main__':
    unittest.main()
