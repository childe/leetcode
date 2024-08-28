#!/usr/bin/env python3
"""
https://leetcode.cn/problems/binary-tree-maximum-path-sum/description/
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float("-inf")

        def post_order(root):
            nonlocal ans
            if not root:
                return float("-inf")
            left = post_order(root.left)
            right = post_order(root.right)
            ans = max(
                ans,
                left,
                right,
                root.val,
                root.val + left,
                root.val + right,
                root.val + left + right,
            )
            return max(root.val, root.val + left, root.val + right)

        post_order(root)
        return ans
