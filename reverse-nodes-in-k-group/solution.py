#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/reverse-nodes-in-k-group/
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
'''

import unittest

# Definition for singly-linked list.


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def printList(self, head):
        while head:
            print head.val,
            head = head.next
        print

    def reverseNextKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode,ListNode,ListNode(head, tail, nexthead)
        >>> nodes = 0->1->2->3
        >>> reverseNextKGroup(head,2)
        0<-1<-2 3
        return 2,0,3

        >>> nodes = 0->1
        >>> reverseNextKGroup(head,3)
        0->1
        return 0,None,None
        """
        t = head
        for i in range(k):
            if t is None:
                return head, None, None
            t = t.next

        pre = None
        q = head
        for i in range(k):
            n = q.next
            q.next = pre
            pre = q
            q = n
        return pre, head, q

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k <= 0:
            return head

        head, tail, nexthead = self.reverseNextKGroup(head, k)
        if tail is None:
            return head
        final_head = head

        while tail is not None:
            _head, _tail, _nexthead = self.reverseNextKGroup(nexthead, k)
            tail.next = _head
            tail, nexthead = _tail, _nexthead

        return final_head


class TestSolution(unittest.TestCase):

    def createList(self, *args):
        if len(args) == 0:
            return None
        head = ListNode(args[0])
        p = head
        for e in args[1:]:
            p.next = ListNode(e)
            p = p.next
        return head

    def NodeList2List(self, nodelist, count=-1):
        rst = []
        n = nodelist
        c = 0
        while n is not None:
            rst.append(n.val)
            n = n.next
            c += 1
            if count != -1 and c >= count:
                break

        return rst

    def test_reverseNextKGroup(self):
        s = Solution()

        l = self.createList(*range(1))
        head, tail, nexthead = s.reverseNextKGroup(l, 3)
        rst_head = self.createList(0)
        self.assertEqual(self.NodeList2List(rst_head), self.NodeList2List(head))
        self.assertEqual(tail, None)
        self.assertEqual(nexthead, None)

        l = self.createList(*range(2))
        head, tail, nexthead = s.reverseNextKGroup(l, 3)
        rst_head = self.createList(0, 1)
        self.assertEqual(self.NodeList2List(rst_head), self.NodeList2List(head))
        self.assertEqual(tail, None)
        self.assertEqual(nexthead, None)

        l = self.createList(*range(3))
        head, tail, nexthead = s.reverseNextKGroup(l, 3)
        self.assertEqual(self.NodeList2List(head), [2, 1, 0])
        self.assertEqual(self.NodeList2List(tail), [0])
        self.assertEqual(self.NodeList2List(nexthead), [])

        l = self.createList(*range(8))
        head, tail, nexthead = s.reverseNextKGroup(l, 3)
        self.assertEqual(self.NodeList2List(head), [2, 1, 0])
        self.assertEqual(self.NodeList2List(tail), [0])
        self.assertEqual(self.NodeList2List(nexthead), [3, 4, 5, 6, 7])

    def test_reverseKGroup(self):
        s = Solution()

        l = self.createList(*range(1))
        head = s.reverseKGroup(l, 3)
        self.assertEqual(self.NodeList2List(head), [0])

        l = self.createList(*range(4))
        head = s.reverseKGroup(l, 3)
        self.assertEqual(self.NodeList2List(head), [2, 1, 0, 3])

        l = self.createList(*range(4))
        head = s.reverseKGroup(l, 1)
        self.assertEqual(self.NodeList2List(head), [0, 1, 2, 3])

        l = self.createList(*range(7))
        head = s.reverseKGroup(l, 2)
        self.assertEqual(self.NodeList2List(head), [1, 0, 3, 2, 5, 4, 6])

        l = self.createList(*range(6))
        head = s.reverseKGroup(l, 2)
        self.assertEqual(self.NodeList2List(head), [1, 0, 3, 2, 5, 4])


if __name__ == '__main__':
    unittest.main()
