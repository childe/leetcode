# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/add-two-numbers-ii/description/
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        l1_length = 0
        n = l1
        while n:
            l1_length += 1
            n = n.next

        l2_length = 0
        n = l2
        while n:
            l2_length += 1
            n = n.next

        if l1_length < l2_length:
            short, far = l1, l2
            diff = l2_length - l1_length
        else:
            short, far = l2, l1
            diff = l1_length - l2_length

        ns, nf, head = short, far, ListNode(0)
        n = head
        for i in range(diff):
            n.next = ListNode(nf.val)
            n = n.next
            nf = nf.next

        # print 'ns',
        # printList(ns)

        # print 'nf',
        # printList(nf)

        # print 'head',
        # printList(head)

        while ns:
            n.next = ListNode(nf.val+ns.val)
            n = n.next
            nf = nf.next
            ns = ns.next

        # print 'head',
        # printList(head)

        changed = True
        while changed:
            p, n, changed = head, head.next, False
            while n:
                if n.val >= 10:
                    p.val += n.val // 10
                    n.val %= 10
                    changed = True
                p = p.next
                n = n.next

        if head.val > 0:
            return head
        return head.next


def createList(l):
    head = ListNode(0)
    n = head
    for i in l:
        n.next = ListNode(i)
        n = n.next

    return head.next


def printList(l):
    while l:
        print l.val,
        l = l.next
    print


def main():
    s = Solution()

    l1 = createList([7, 2, 4, 3])
    printList(l1)

    l2 = createList([5, 6, 4])
    printList(l2)

    head = s.addTwoNumbers(l1, l2)
    printList(head)


if __name__ == '__main__':
    main()
