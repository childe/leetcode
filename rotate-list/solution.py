#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

'''
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
'''

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or k == 0:
            return head

        p, length = head, 1
        while p.next:
            p = p.next
            length += 1
        tail, p = p, head

        if k % length == 0:
            return head

        # print length, tail.val

        offset = length - k % length
        for i in range(offset-1):
            p = p.next

        newHead, p.next, tail.next = p.next, None, head

        return newHead


def genList(s, e):
    head = ListNode(s)
    tail = head
    for i in range(s+1, e+1):
        tail.next = ListNode(i)
        tail = tail.next
    return head


def genArray(head):
    '''
    >>> genArray(genList(0,9)) == range(10)
    True
    >>> genArray(genList(1,5)) == range(1,6)
    True
    '''
    p = head
    rst = []
    while p:
        rst.append(p.val)
        p = p.next
    return rst


class TestSolution(unittest.TestCase):

    def test_rotateRight(self):
        s = Solution()

        rst = s.rotateRight(genList(1, 2), 2)
        self.assertEqual(genArray(rst), [1, 2])

        rst = s.rotateRight(genList(1, 1), 1)
        self.assertEqual(genArray(rst), [1])

        rst = s.rotateRight(genList(1, 5), 2)
        self.assertEqual(genArray(rst), [4, 5, 1, 2, 3])

        rst = s.rotateRight(genList(0, 2), 4)
        self.assertEqual(genArray(rst), [2, 0, 1])

        rst = s.rotateRight(genList(1, 1), 0)
        self.assertEqual(genArray(rst), [1])


if __name__ == '__main__':
    unittest.main()
