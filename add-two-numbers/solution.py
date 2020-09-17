# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        node = head
        plus = 0
        while l1 and l2:
            n = l1.val + l2.val + plus
            node.next = ListNode(n % 10)
            node = node.next
            plus = n // 10
            l1 = l1.next
            l2 = l2.next
        if l1 is None:
            l = l2
        else:
            l = l1

        while l:
            n = l.val + plus
            node.next = ListNode(n % 10)
            node = node.next
            plus = n // 10
            l = l.next
        if plus:
            node.next = ListNode(1)
        return head.next
