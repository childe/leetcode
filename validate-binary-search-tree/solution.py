#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/validate-binary-search-tree/description/

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:

Input:
    2
   / \
  1   3
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value is 5 but its right child's value is 4.
"""


class TreeNode(object):
    '''
    Definition for a binary tree node.
    '''

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValid(self, root, minValue, maxValue):
        """
        :type root: TreeNode
        :type minValue: int
        :type maxValue: int
        :rtype: bool
        """
        if root is None:
            return True
        if root.val >= maxValue or root.val <= minValue:
            return False
        return self.isValid(root.left, minValue, root.val) and self.isValid(root.right, root.val, maxValue)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        l, r = root, root
        while l.left:
            l = l.left
        while r.right:
            r = r.right
        return self.isValid(root, l.val-1, r.val+1)


def main():
    s = Solution()

    root = TreeNode(1)
    root.left = TreeNode(1)

    print s.isValidBST(root)


if __name__ == '__main__':
    main()
