#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/reverse-nodes-in-k-group/
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
"""

import unittest

# Definition for singly-linked list.


class ListNode(object):

    def __init__(self, x):
        self.val: int = x
        self.next: ListNode | None = None

    def __str__(self) -> str:
        if self.next:
            return f"{self.val}->{self.next.val}"
        return f"{self.val}"


class Solution(object):
    def reverseNextKGroup(self, head, k) -> tuple[ListNode, ListNode | None, bool]:
        """
        return new_head, next_head, is_reversed
        >>> nodes = 0->1->2->3
        >>> reverseNextKGroup(head,3)
        0<-1<-2 3
        return 2, 3, True

        >>> nodes = 0->1
        >>> reverseNextKGroup(head,3)
        0->1
        return 0, None, False

        >>> nodes = 0->1->2
        >>> reverseNextKGroup(head,3)
        0<-1<-2
        return 0, None, True
        """

        # t, _array_for_test = head, []
        # while t:
        # _array_for_test.append(t)
        # t = t.next

        if not head:
            return head, None, False

        t = head
        for _ in range(k - 1):
            t = t.next
            if t is None:
                return head, None, False

        c = head
        for _ in range(k - 1):
            # print(",".join([str(node) for node in _array_for_test]))
            n = head.next
            head.next = n.next
            n.next = c
            c = n
            # print(c)
        # print(",".join([str(node) for node in _array_for_test]))
        return c, head.next, True

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k <= 1:
            return head

        final_head, next_head, is_reversed = self.reverseNextKGroup(head, k)
        if not is_reversed:
            return head

        last_tail = head
        while is_reversed and next_head:
            _t = next_head
            new_head, next_head, is_reversed = self.reverseNextKGroup(next_head, k)
            last_tail.next = new_head
            last_tail = _t

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
        head, nexthead, is_reversed = s.reverseNextKGroup(l, 1)
        self.assertEqual(self.NodeList2List(head), [0])
        self.assertEqual(head.val, 0)
        self.assertEqual(nexthead, None)
        self.assertEqual(is_reversed, True)

        l = self.createList(*range(1))
        head, nexthead, is_reversed = s.reverseNextKGroup(l, 3)
        self.assertEqual(self.NodeList2List(head), [0])
        self.assertEqual(head.val, 0)
        self.assertEqual(nexthead, None)
        self.assertEqual(is_reversed, False)

        l = self.createList(*range(2))
        head, nexthead, is_reversed = s.reverseNextKGroup(l, 3)
        self.assertEqual(self.NodeList2List(head), [0, 1])
        self.assertEqual(head.val, 0)
        self.assertEqual(nexthead, None)
        self.assertEqual(is_reversed, False)

        l = self.createList(*range(3))
        head, nexthead, is_reversed = s.reverseNextKGroup(l, 3)
        self.assertEqual(self.NodeList2List(head), [2, 1, 0])
        self.assertEqual(head.val, 2)
        self.assertEqual(nexthead, None)
        self.assertEqual(is_reversed, True)

        l = self.createList(*range(4))
        head, nexthead, is_reversed = s.reverseNextKGroup(l, 3)
        self.assertEqual(self.NodeList2List(head), [2, 1, 0, 3])
        self.assertEqual(head.val, 2)
        assert nexthead is not None
        self.assertEqual(nexthead.val, 3)
        self.assertEqual(is_reversed, True)

        l = self.createList(*range(5))
        head, nexthead, is_reversed = s.reverseNextKGroup(l, 3)
        self.assertEqual(self.NodeList2List(head), [2, 1, 0, 3, 4])
        self.assertEqual(head.val, 2)
        assert nexthead is not None
        self.assertEqual(nexthead.val, 3)
        self.assertEqual(is_reversed, True)

    def test_reverseKGroup(self):
        s = Solution()

        l = self.createList(*range(5))
        head = s.reverseKGroup(l, 2)
        self.assertEqual(self.NodeList2List(head), [1, 0, 3, 2, 4])

        l = self.createList(*range(1))
        head = s.reverseKGroup(l, 3)
        self.assertEqual(self.NodeList2List(head), [0])

        l = self.createList(*range(4))
        head = s.reverseKGroup(l, 3)
        self.assertEqual(self.NodeList2List(head), [2, 1, 0, 3])

        l = self.createList(*range(4))
        head = s.reverseKGroup(l, 1)
        self.assertEqual(self.NodeList2List(head), [0, 1, 2, 3])

        l = self.createList(*range(6))
        head = s.reverseKGroup(l, 2)
        self.assertEqual(self.NodeList2List(head), [1, 0, 3, 2, 5, 4])


if __name__ == "__main__":
    unittest.main()
