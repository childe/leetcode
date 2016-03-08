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

    def reverse(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        >>> s = Solution()
        >>> head = ListNode(0)
        >>> c = head
        >>> for i in range(1,9):
        ...   c.next = ListNode(i)
        ...   c = c.next
        >>> r = []
        >>> c = head
        >>> while (c):
        ...   r.append(c.val)
        ...   c = c.next
        >>> r
        [0, 1, 2, 3, 4, 5, 6, 7, 8]

        >>> head = s.reverse(head)
        >>> r = []
        >>> c = head
        >>> while (c):
        ...   r.append(c.val)
        ...   c = c.next
        >>> r
        [8, 7, 6, 5, 4, 3, 2, 1, 0]

        >>> head = ListNode(0)
        >>> head = s.reverse(head)
        >>> head.val
        0
        >>> head.next is None
        True
        """
        pre_node = None
        current_node = head
        while (current_node is not None):
            _next_node = current_node.next
            current_node.next = pre_node
            pre_node = current_node
            current_node = _next_node
        return pre_node


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

        head = self.reverse(head)
        pre_node = None
        current_node = head
        i = 1
        while(current_node):
            if i == n:
                if current_node.next is not None:
                    _next_node = current_node.next.next
                    current_node.next.next = pre_node
                    pre_node = current_node.next
                    current_node = _next_node
                else:
                    break
            else:
                _next_node = current_node.next
                current_node.next = pre_node
                pre_node = current_node
                current_node = _next_node

            i += 1

        return pre_node
