# !/usr/bin/env python
# -*- coding: utf-8 -*-
'''
https://leetcode.com/problems/merge-k-sorted-lists/

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
'''

import unittest

# Definition for singly-linked list.


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def printList(self, head):
        while head:
            print head.val,
            head = head.next
        print

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return

        for i,l in enumerate(lists):
            if l is not None:
                head = l
                rest = lists[i+1:]
                break
        else:
            return None
        for current_process_node in rest:
# 对后续每一个链表(1), 合并到之前已经合并过的链表中(0)
            # print "\n###\nlist 0 is",
            # self.printList(head)
            # print "now process",
            # self.printList(current_process_node)
            # print
            p = None
            o = head
            while current_process_node is not None:
                # print "current_process_node is", current_process_node.val
                while o is not None:
                    # print p.val if p else "none", o.val, current_process_node.val
                    if current_process_node.val > o.val:
# 链表1的当前节点比链表0中的节点要大, 继续遍历链表0
                        p = o
                        o = o.next
                        continue
# 链表1的当前节点, 比链表0中的节点要小, 插入链表0, 并继续遍历链表1
                    n = current_process_node.next
                    current_process_node.next = o
                    if p is None:
                        head = current_process_node
                    else:
                        p.next = current_process_node
                    p = current_process_node
                    current_process_node = n
                    if n is None:
# 链表1已经遍历到了最后
                        break
                else:
# 没有break, 说明链表0已经遍历到了最后,如果链表1中还有元素, 插入到链表0最后
                    p.next = current_process_node
                    current_process_node = None #已经没必要再遍历链表1了


        return head


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

    def NodeLists2List(self, *nodelists):
        rst = []
        for e in nodelists:
            rst.extend(self.NodeList2List(e))
        return rst

    def NodeList2List(self, nodelist):
        rst = []
        n = nodelist
        while n is not None:
            rst.append(n.val)
            n = n.next

        return rst

    def testMergeKLists(self):
        s = Solution()

        l1 = self.createList()
        l2 = self.createList(1)
        rst = self.createList(1)
        myrst = s.mergeKLists([l1, l2])
        # s.printList(rst)
        # s.printList(myrst)
        # print
        self.assertEqual(self.NodeList2List(rst), self.NodeList2List(myrst))

        l1 = self.createList(1)
        l2 = self.createList()
        rst = self.createList(1)
        myrst = s.mergeKLists([l1, l2])
        # s.printList(rst)
        # s.printList(myrst)
        # print
        self.assertEqual(self.NodeList2List(rst), self.NodeList2List(myrst))

        l1 = self.createList(1, 3, 5)
        l2 = self.createList(2, 4)
        rst = self.createList(1, 2, 3, 4, 5)
        myrst = s.mergeKLists([l1, l2])
        # s.printList(rst)
        # s.printList(myrst)
        # print
        self.assertEqual(self.NodeList2List(rst), self.NodeList2List(myrst))

        l1 = self.createList(1, 2, 3)
        l2 = self.createList(2, 4, 6)
        rst = self.createList(1, 2, 2, 3, 4, 6)
        myrst = s.mergeKLists([l1, l2])
        # s.printList(rst)
        # s.printList(myrst)
        # print
        self.assertEqual(self.NodeList2List(rst), self.NodeList2List(myrst))

        l1 = self.createList(1, 3, 5)
        l2 = self.createList(2, 4, 6)
        l3 = self.createList(1, 4)
        rst = self.createList(1, 1, 2, 3, 4, 4, 5, 6)
        myrst = s.mergeKLists([l1, l2, l3])
        # s.printList(rst)
        # s.printList(myrst)
        # print
        self.assertEqual(self.NodeList2List(rst), self.NodeList2List(myrst))

        l1 = self.createList(1, 3, 5)
        l2 = self.createList(2, 4, 8)
        l3 = self.createList(1, 7)
        rst = self.createList(1,1,2, 3, 4, 5,7,8)
        myrst = s.mergeKLists([l1, l2, l3])
        # s.printList(rst)
        # s.printList(myrst)
        # print
        self.assertEqual(self.NodeList2List(rst), self.NodeList2List(myrst))

        l1 = self.createList(1, 3, 5)
        rst = self.createList(1, 3, 5)
        myrst = s.mergeKLists([l1])
        # s.printList(rst)
        # s.printList(myrst)
        # print
        self.assertEqual(self.NodeList2List(rst), self.NodeList2List(myrst))

        import random
        nodelists = []
        for i in range(10000):
            nodelists.append(ListNode(random.randint(1,100)))
        myrst = s.mergeKLists(nodelists)
        # self.assertEqual(self.NodeList2List(rst), self.NodeLists2List(*nodelists))


if __name__ == '__main__':
    unittest.main()
