#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

https://leetcode.com/problems/copy-list-with-random-pointer/description/

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.


'''

# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """

        if head is None:
            return None

        new_head = RandomListNode(head.label)
        allNodes = {head.label: new_head}
        n = head
        while n:
            new_node = allNodes[n.label]
            if n.next:
                nextNode = allNodes.get(n.next.label, RandomListNode(n.next.label))
                allNodes.setdefault(nextNode.label, nextNode)
                new_node.next = nextNode

            if n.random:
                randomNode = allNodes.get(n.random.label, RandomListNode(n.random.label))
                allNodes.setdefault(randomNode.label, randomNode)
                new_node.random = randomNode

            n = n.next

        return new_head
