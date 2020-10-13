# -*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/

82. Remove Duplicates from Sorted List II
Given a sorted linked list, delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list.

Return the linked list sorted as well.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def findLastSameValNode(self, node):
        while node.next and node.next.val == node.val:
            node = node.next

        return node

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        sentinel = ListNode(None)
        sentinel.next = node = head
        pre = sentinel
        while node:
            # print(pre.val, node.val)
            lastSameValNode = self.findLastSameValNode(node)
            if node is lastSameValNode:
                pre = node
                node = node.next
            else:
                # raise BaseException(str(node.val))
                pre.next = node = lastSameValNode.next

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
    head = genList([1, 2, 3, 3, 4, 4, 5])
    l = encodeList(head)
    head = s.deleteDuplicates(head)
    l = encodeList(head)
    print(l)
    assert l == [1, 2, 5]

    head = genList([1, 1, 1, 2, 3])
    l = encodeList(head)
    head = s.deleteDuplicates(head)
    l = encodeList(head)
    print(l)
    assert l == [2, 3]


if __name__ == "__main__":
    main()
