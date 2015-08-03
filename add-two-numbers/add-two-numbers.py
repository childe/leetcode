#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""https://leetcode.com/problems/add-two-numbers/
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""

import unittest


# Definition for singly-linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    """
    """

    # @param {ListNode} l
    # @return {ListNode}

    def _reverse_linked_list(self, l):
        if l is None:
            return l
        n = l.next
        l.next = None
        while(n):
            nn = n.next
            n.next = l

            l = n
            n = nn

        return l

    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        #l1 = self._reverse_linked_list(l1)
        #l2 = self._reverse_linked_list(l2)

        head, current = None,None
        carry = 0
        while(l1 or l2):
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            s = v1+v2+carry
            carry, s = s/10, s % 10

            node = ListNode(s)

            if head is None:
                head = node
            else:
                current.next=node

            current=node

        if carry == 1:
            current.next = ListNode(carry)

        return head


class TestSolution(unittest.TestCase):

    def test_reverse(self):
        s = Solution()
        l = ListNode(0)
        h = l
        for i in range(1, 5):
            l.next = ListNode(i)
            l = l.next
        h = s._reverse_linked_list(h)

        rst = []
        while(h):
            rst.append(h.val)
            h = h.next

        self.assertEqual(rst,[4,3,2,1,0])

    def test_addTwoNumbers(self):
        s = Solution()

        # 1
        l1 =[ListNode(e) for e in [2,4,3]]
        for idx,node in enumerate(l1[:-1]):
            node.next = l1[idx+1]

        l2 =[ListNode(e) for e in [5,6,4]]
        for idx,node in enumerate(l2[:-1]):
            node.next = l2[idx+1]

        rst = s.addTwoNumbers(l1[0],l2[0])
        while(rst):
            print rst.val
            rst=rst.next
        print

        # 2
        l1 =[ListNode(e) for e in [1,2,4,3]]
        for idx,node in enumerate(l1[:-1]):
            node.next = l1[idx+1]

        l2 =[ListNode(e) for e in [5,6,4]]
        for idx,node in enumerate(l2[:-1]):
            node.next = l2[idx+1]

        rst = s.addTwoNumbers(l1[0],l2[0])
        while(rst):
            print rst.val
            rst=rst.next
        print

        # 2
        l1 =[ListNode(e) for e in [5]]
        for idx,node in enumerate(l1[:-1]):
            node.next = l1[idx+1]

        l2 =[ListNode(e) for e in [5]]
        for idx,node in enumerate(l2[:-1]):
            node.next = l2[idx+1]

        rst = s.addTwoNumbers(l1[0],l2[0])
        while(rst):
            print rst.val
            rst=rst.next


if __name__ == '__main__':
    unittest.main()
