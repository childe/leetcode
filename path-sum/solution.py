#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/path-sum/

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22
"""

import unittest

# Definition for a binary tree node.


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)


class Solution(object):

    def hasPathSum2(self, root, sum_value):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        recursion
        """
        if root is None:
            return False
        if root.left is None and root.right is None:
            return root.val is sum_value
        return self.hasPathSum2(
            root.left,
            sum_value -
            root.val) or self.hasPathSum2(
            root.right,
            sum_value -
            root.val)

    def hasPathSum(self, root, sum_value):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False

        last_poped = False
        journey = [(root, root.val)]  # node, root_to_this_sum
        while journey:
            node, s = journey[-1][0], journey[-1][1]
            if not node.left and not node.right:
                if s == sum_value:
                    return True
                else:
                    last_poped = journey.pop()[0]

            if node.left is last_poped or node.right is last_poped:
                last_poped = journey.pop()[0]
                continue

            if node.left and node.left is not last_poped:
                journey.append((node.left, s + node.left.val))
            if node.right and node.right is not last_poped:
                journey.append((node.right, s + node.right.val))

        return False


class TestSolution(unittest.TestCase):

    def test_hasPathSum(self):
        s = Solution()

        root = TreeNode(10)
        root.right = TreeNode(20)
        my_answer = s.hasPathSum(root, 31)
        answer = s.hasPathSum2(root, 31)
        self.assertEqual(my_answer, answer)

        root = TreeNode(10)
        root.right = TreeNode(20)
        my_answer = s.hasPathSum(root, 30)
        answer = s.hasPathSum2(root, 30)
        self.assertEqual(my_answer, answer)

        root = TreeNode(10)
        my_answer = s.hasPathSum(root, 11)
        answer = s.hasPathSum2(root, 11)
        self.assertEqual(my_answer, answer)

        root = TreeNode(10)
        my_answer = s.hasPathSum(root, 10)
        answer = s.hasPathSum2(root, 10)
        self.assertEqual(my_answer, answer)

        import random

        def build_tree(node_count):
            if node_count == 0:
                return None
            left_count = random.randint(0, node_count-1)
            right_count = node_count-1-left_count
            root = TreeNode(random.randint(1, 100))
            root.left = build_tree(left_count)
            root.right = build_tree(right_count)
            return root

        def tree_node_count(root):
            rst = 0
            l = [root]
            while (l):
                n = l.pop()
                rst += 1
                if n.left:
                    l.append(n.left)
                if n.right:
                    l.append(n.right)
            return rst

        root = build_tree(100)
        for i in range(100*100):
            my_answer = s.hasPathSum(root, i)
            answer = s.hasPathSum2(root, i)
            self.assertEqual(my_answer, answer)


if __name__ == '__main__':
    unittest.main()
