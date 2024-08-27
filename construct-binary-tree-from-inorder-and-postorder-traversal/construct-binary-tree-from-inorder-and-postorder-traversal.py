#!/usr/bin/env python3
"""
https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        for i, node in enumerate(inorder):
            if node == postorder[-1]:
                root = TreeNode(node)
                root.left = self.buildTree(inorder[:i], postorder[:i])
                root.right = self.buildTree(inorder[i + 1 :], postorder[i:-1])
                return root
        return None


import unittest


class TestSolution(unittest.TestCase):
    def test_buildTree(self):
        inorder = [9, 3, 15, 20, 7]
        postorder = [9, 15, 7, 20, 3]
        root = Solution().buildTree(inorder, postorder)
        self.assertEqual(root.val, 3)
        self.assertEqual(root.left.val, 9)
        self.assertEqual(root.right.val, 20)
        self.assertEqual(root.right.left.val, 15)
        self.assertEqual(root.right.right.val, 7)


if __name__ == "__main__":
    unittest.main()
