# -*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/median-of-two-sorted-arrays/

"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if not nums1:
            return nums2[(len(nums2) - 1) // 2]
        if not nums2:
            return nums1[(len(nums1) - 1) // 2]

        i, j, m = 0, 0, (len(nums1) + len(nums2) - 1) // 2
        while (i + j) < m:
            if nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        print(i, j)
        if nums2[j] < nums1[i]:
            i, j = j, i
            nums1, nums2 = nums2, nums1

        if (len(nums1) + len(nums2) % 2) == 1:
            return nums1[i]
        if i == len(nums1) - 1:
            return (nums1[i] + nums2[j]) / 2
        return (nums1[i] + min(nums2[j], nums1[i + 1])) / 2


def main():
    s = Solution()

    nums1 = [1, 3]
    nums2 = [2]
    ans = s.findMedianSortedArrays(nums1, nums2)
    print(ans)
    assert ans == 2.0

    nums1 = [1, 2]
    nums2 = [3, 4]
    ans = s.findMedianSortedArrays(nums1, nums2)
    print(ans)
    assert ans == 2.5

    nums1 = [0, 0]
    nums2 = [0, 0]
    ans = s.findMedianSortedArrays(nums1, nums2)
    print(ans)
    assert ans == 0.0

    nums1 = []
    nums2 = [1]
    ans = s.findMedianSortedArrays(nums1, nums2)
    print(ans)
    assert ans == 1.0

    nums1 = [2]
    nums2 = []
    ans = s.findMedianSortedArrays(nums1, nums2)
    print(ans)
    assert ans == 2.0


if __name__ == "__main__":
    main()
