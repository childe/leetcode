# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/reorder-list/description/

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
"""
# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        l, n = 0, head
        while n:
            l += 1
            n = n.next

        if l <= 2:
            return

        p = head
        for i in range((l-1)//2):
            p = p.next

        q = p.next
        p.next = None

        p = q
        q = p.next

        p.next = None

        while q:
            qq = q.next
            q.next = p
            p, q = q, qq

        n = head
        while p:
            q = p.next
            p.next = n.next
            n.next = p

            n = p.next
            p = q



def printList(n):
    while n:
        print n.val,
        n = n.next
    print


def createList(nums):
    if len(nums) == 0:
        return None
    head = ListNode(nums[0])
    p = head
    for e in nums[1:]:
        p.next = ListNode(e)
        p = p.next
    return head


def main():
    s = Solution()

    l = createList(range(1, 6))
    printList(l)
    s.reorderList(l)
    printList(l)

    l = createList(range(1, 5))
    printList(l)
    s.reorderList(l)
    printList(l)

    l = createList(range(1, 1))
    printList(l)
    s.reorderList(l)
    printList(l)

    l = createList(range(1, 2))
    printList(l)
    s.reorderList(l)
    printList(l)

    l = createList(range(1, 3))
    printList(l)
    s.reorderList(l)
    printList(l)

if __name__ == '__main__':
    main()
