#!/usr/bin/env python3

"""
https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def pre_order_first(node: TreeNode) -> tuple[TreeNode, TreeNode]:
            """
            return (head, tail)
            """
            left, right = node.left, node.right
            if left:
                left_head, left_tail = pre_order_first(left)
                node.left = None
                node.right = left_head
            else:
                left_tail = node
            if right:
                right_head, right_tail = pre_order_first(right)
                if left:
                    left_tail.right = right_head
                return node, right_tail
            else:
                return node, left_tail

        if root:
            pre_order_first(root)
