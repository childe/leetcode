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
        if head is None:
            return

        # find mid node & reverse first half list
        p, q, skip_p = head, head.next, head.next
        head.next = None
        while skip_p and skip_p.next:
            skip_p = skip_p.next.next

            qq, q.next = q.next, p
            p, q = q, qq

        # reorder
        if skip_p is None:
            last_p, p = p, p.next
            last_p.next = None
        else:
            last_p = None

        while p:
            pn, qn = p.next, q.next
            p.next, q.next = q, last_p
            last_p, p, q = p, pn, qn


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

    l = createList(range(1, 7))
    printList(l)
    s.reorderList(l)
    printList(l)

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
