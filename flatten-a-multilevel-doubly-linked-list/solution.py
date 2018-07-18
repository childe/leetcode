# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/description/


You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.

Example:

Input:
 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL

Output:
1-2-3-7-8-11-12-9-10-4-5-6-NULL
Explanation for the above example:

Given the following multilevel doubly linked list:



We should return the following flattened doubly linked list:

"""

# Definition for a Node.


class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return

        stack = [head]
        lastNode = None
        while stack:
            node = stack.pop()
            if lastNode:
                lastNode.next = node
                node.prev = lastNode
            while node:
                lastNode = node
                if node.child:
                    if node.next:
                        stack.append(node.next)

                    node.next = node.child
                    node.child = None
                    node.next.prev = node
                node = node.next

        return head
