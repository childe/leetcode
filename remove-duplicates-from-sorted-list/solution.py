# -*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/

83. Remove Duplicates from Sorted List
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        sentinel = ListNode(None)
        sentinel.next = node = head
        while node and node.next:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next

        return sentinel.next


def genList(l):
    sentinel = ListNode(0)
    node = sentinel
    for n in l:
        node.next = ListNode(n)
        node = node.next

    return sentinel.next


def encodeList(node):
    l = []
    while node:
        l.append(node.val)
        node = node.next
    return l


def main():
    s = Solution()
    head = genList([1, 1, 2])
    head = s.deleteDuplicates(head)
    print(encodeList(head))

    head = genList([1, 1, 2, 3, 3])
    head = s.deleteDuplicates(head)
    print(encodeList(head))


if __name__ == "__main__":
    main()
