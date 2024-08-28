#!/usr/bin/env python3
"""
https://leetcode.cn/problems/sum-root-to-leaf-numbers/description/
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if not node:
                return
            if not node.left and not node.right:
                yield str(node.val)
            for n in helper(node.left):
                yield str(node.val) + n
            for n in helper(node.right):
                yield str(node.val) + n

        return sum([int(e) for e in helper(root)])
