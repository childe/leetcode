#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/binary-tree-preorder-traversal/description/

Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]

        >>> root = TreeNode(1)
        >>> root.right = TreeNode(2)
        >>> root.right.left = TreeNode(3)
        >>> s = Solution()
        >>> s.preorderTraversal(root)
        [1, 2, 3]
        >>> root = TreeNode(1)
        >>> s = Solution()
        >>> s.preorderTraversal(root)
        [1]
        """
        if root is None:
            return []

        rst = []
        stack = [root]
        while stack:
            currentNode = stack.pop()
            rst.append(currentNode.val)
            if currentNode.right is not None:
                stack.append(currentNode.right)
            if currentNode.left is not None:
                stack.append(currentNode.left)

        return rst
