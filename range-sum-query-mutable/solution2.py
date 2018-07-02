#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/range-sum-query-mutable/description/

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.

Example:
Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:

The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.
'''


class Node(object):
    def __init__(self, value, idx, left, right, sumValue):
        self.idx = idx
        self.value = value
        self.l = left
        self.r = right
        self.sumValue = sumValue


def createTree(nums, left, right):
    """
    :type nums: List[int]
    :type left: int
    :type right: int
    :rtype: Node
    >>> t = createTree(range(1), 0 , 0)
    >>> t.sumValue
    0
    >>> t.idx
    0
    >>> t = createTree(range(2), 1 , 1)
    >>> t.sumValue
    1
    >>> t.idx
    1
    >>> t = createTree(range(2), 0 , 1)
    >>> t.sumValue
    1
    >>> t = createTree(range(10), 0 , 9)
    >>> t.sumValue
    45
    >>> t.value
    4
    >>> t.idx
    4
    >>> t.l.sumValue
    6
    >>> t.r.sumValue
    35
    >>> t.l.l.value
    0
    >>> t.l.l.sumValue
    0
    """
    if left == right:
        return Node(nums[left], left, None, None, nums[left])
    mid = (left + right) / 2

    if mid > left:
        l = createTree(nums, left, mid-1)
        leftSum = l.sumValue
    else:
        l = None
        leftSum = 0

    r = createTree(nums, mid+1, right)
    rightSum = r.sumValue

    return Node(nums[mid], mid, l, r, leftSum + rightSum + nums[mid])


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        if nums == []:
            self.root = None
            return
        self.root = createTree(nums, 0, len(nums)-1)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        >>> s = NumArray(range(10))
        >>> s.sumRange(0, 9)
        45
        >>> s.update(4, 0)
        >>> s.sumRange(0, 9)
        41
        >>> s.sumRange(1, 8)
        32
        """
        if i >= len(self.nums):
            return
        n, diff, self.nums[i] = self.root, val-self.nums[i], val
        while n.idx != i:
            n.sumValue += diff
            if n.idx < i:
                n = n.r
            else:
                n = n.l
        n.value = val
        n.sumValue += diff

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        >>> s = NumArray(range(10))
        >>> s.sumRange(0, 9)
        45
        >>> s.sumRange(1, 8)
        36
        >>> s = NumArray(list(reversed(range(10))))
        >>> s.sumRange(0, 9)
        45
        >>> s.sumRange(1, 8)
        36
        >>> s = NumArray([9, -8])
        >>> s.root.sumValue
        1
        >>> s.root.l is None
        True
        >>> s.root.r.sumValue
        -8
        >>> s.root.r.value
        -8
        >>> s.sumRange(1, 1)
        -8
        >>> s.update(0, 3)
        >>> s.sumRange(1, 1)
        -8
        """
        if i < 0:
            i = 0
        if j >= len(self.nums):
            j = len(self.nums)-1

        # find common root
        cr = self.root
        while cr.idx < i:
            cr = cr.r
        while cr.idx > j:
            cr = cr.l

        sumValue = cr.sumValue
        # look for left idx
        n = cr
        while n.idx != i:
            if n.idx > i:
                n = n.l
            else:
                sumValue = sumValue - n.value - (n.l.sumValue if n.l else 0)
                n = n.r
        sumValue = sumValue - (n.l.sumValue if n.l else 0)

        n = cr
        while n.idx != j:
            if n.idx > j:
                sumValue = sumValue - n.value - (n.r.sumValue if n.r else 0)
                n = n.l
            else:
                n = n.r
        sumValue = sumValue - (n.r.sumValue if n.r else 0)

        return sumValue


def main():
    import sys

    s = NumArray([1, 9, 5, 7, 3])
    print s.sumRange(1, 2)


if __name__ == '__main__':
    main()
