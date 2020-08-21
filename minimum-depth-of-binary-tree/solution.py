# -*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/

111. Minimum Depth of Binary Tree
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
    return its minimum depth = 2.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        stack = [(root, 1)]
        while stack:
            node, depth = stack.pop()
            if node.left is None and node.right is None:
                return depth
            if node.left is not None:
                stack.insert(0, (node.left, depth + 1))
            if node.right is not None:
                stack.insert(0, (node.right, depth + 1))
