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

    def merge2Lists(self, lista, listb):
        """
        :type lista: ListNode
        :type listb: ListNode
        :rtype: ListNode
        """
        if not lista:
            return listb
        if not listb:
            return lista

        pa = None
        oa = lista
        ob = listb
        head = oa if oa.val < ob.val else ob

        while True:
            if oa.val < ob.val:
                # oa 前进1
                pa = oa
                oa = oa.next
                if oa is None:
                    pa.next = ob
                    return head
            else:
                # 把ob插入pa,oa之间. pa->ob. ob->ob.next
                # ob 前进1
                n = ob.next
                ob.next = oa
                if pa is not None:
                    pa.next = ob
                pa = ob
                ob = n
                if ob is None:
                    return head

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return

        if len(lists) == 2:
            return self.merge2Lists(*lists)
        if len(lists) == 1:
            return lists[0]

        mid = (len(lists)-1)/2
        return self.merge2Lists(
            self.mergeKLists(
                lists[:mid]),
            self.mergeKLists(
                lists[mid:]))


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

    def testMerge2Lists(self):
        self.maxDiff = None

        s = Solution()
        l1 = self.createList()
        l2 = self.createList(1)
        rst = sorted(self.NodeLists2List(l1, l2))
        myrst = s.merge2Lists(l1, l2)
        self.assertEqual(rst, self.NodeList2List(myrst))

        l1 = self.createList(1)
        l2 = self.createList()
        rst = sorted(self.NodeLists2List(l1, l2))
        myrst = s.merge2Lists(l1, l2)
        self.assertEqual(rst, self.NodeList2List(myrst))

        l1 = self.createList(1)
        l2 = self.createList(1, 1, 1, 1)
        rst = sorted(self.NodeLists2List(l1, l2))
        myrst = s.merge2Lists(l1, l2)
        self.assertEqual(rst, self.NodeList2List(myrst))

        import random
        for i in range(100):
            l1 = self.createList(
                *
                sorted(
                    [random.randint(1, 100)
                     for i in range(random.randint(1, 100))]))
            l2 = self.createList(
                *
                sorted(
                    [random.randint(1, 100)
                     for i in range(random.randint(1, 100))]))
            # print self.NodeList2List(l1)
            # print self.NodeList2List(l2)

            rst = sorted(self.NodeLists2List(l1, l2))
            # print rst
            myrst = s.merge2Lists(l1, l2)
            self.assertEqual(self.NodeList2List(myrst), rst)

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
        rst = self.createList(1, 1, 2, 3, 4, 5, 7, 8)
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
            nodelists.append(ListNode(random.randint(1, 100)))
        rst = sorted(self.NodeLists2List(*nodelists))
        myrst = s.mergeKLists(nodelists)
        self.assertEqual(self.NodeList2List(myrst), rst)


if __name__ == '__main__':
    unittest.main()
