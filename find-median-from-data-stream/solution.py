#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/find-median-from-data-stream/

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples:
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
For example:

add(1)
add(2)
findMedian() -> 1.5
add(3)
findMedian() -> 2
Credits:
Special thanks to @Louis1992 for adding this problem and creating all test cases.
"""

import unittest
import heapq


class MedianFinder:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.maxheap = []
        self.minheap = []

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if len(self.maxheap) == len(self.minheap):
            n = heapq.heappushpop(self.maxheap, (-num, num))
            heapq.heappush(self.minheap, n[1])
        else:
            n = heapq.heappushpop(self.minheap, num)
            heapq.heappush(self.maxheap, (-n, n))

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if self.minheap == []:
            return
        if len(self.maxheap) == len(self.minheap):
            return (self.maxheap[0][1] + self.minheap[0])/2.0
        return self.minheap[0]


class TestMedianFinder(unittest.TestCase):

    def test_findMedian(self):
        import random
        m = MedianFinder()
        h = []
        n = random.randint(10, 100)
        for i in range(n):
            num = random.randint(1, 100)
            m.addNum(num)
            h.append(num)
        my_answer = m.findMedian()
        h.sort()
        answer = (h[(n-1)/2]+h[n/2])/2.0
        self.assertEqual(my_answer, answer)


if __name__ == '__main__':
    unittest.main()
