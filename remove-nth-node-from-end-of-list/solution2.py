#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

      After removing the second node from the end, the linked list becomes 1->2->3->5.
      Note:
          Given n will always be valid.
          Try to do this in one pass.
'''

# Definition for singly-linked list.


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode

        >>> n1 = ListNode(1)
        >>> n2 = ListNode(2)
        >>> n1.next = n2
        >>> n3 = ListNode(3)
        >>> n2.next = n3
        >>> s = Solution()
        >>> head = s.removeNthFromEnd(n1, 1)
        >>> head.val
        1
        >>> head = head.next
        >>> head.val
        2
        >>> head = head.next
        >>> head is None
        True

        >>> head = ListNode(0)
        >>> c = head
        >>> for i in range(1,9):
        ...   c.next = ListNode(i)
        ...   c = c.next
        >>> head = s.removeNthFromEnd(head,1)
        >>> r = []
        >>> c = head
        >>> while (c):
        ...   r.append(c.val)
        ...   c = c.next
        >>> r
        [0, 1, 2, 3, 4, 5, 6, 7]

        >>> head = ListNode(0)
        >>> c = head
        >>> for i in range(1,9):
        ...   c.next = ListNode(i)
        ...   c = c.next
        >>> head = s.removeNthFromEnd(head,2)
        >>> r = []
        >>> c = head
        >>> while (c):
        ...   r.append(c.val)
        ...   c = c.next
        >>> r
        [0, 1, 2, 3, 4, 5, 6, 8]

        >>> head = ListNode(1)
        >>> head = s.removeNthFromEnd(head,1)
        >>> head is None
        True
        """

        if n <= 0:
            return head

        if head is None:
            return head

        ahead_node = head
        for i in range(n-1):
            ahead_node = ahead_node.next
            if ahead_node is None:
                return head

        posterior_node = ListNode(None)
        posterior_node.next = head
        head = posterior_node
        while ahead_node.next is not None:
            ahead_node = ahead_node.next
            posterior_node = posterior_node.next

        posterior_node.next= posterior_node.next.next
        return head.next
