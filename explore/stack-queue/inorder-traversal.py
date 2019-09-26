# -*- coding: utf-8 -*-

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        r = []

        s = [(0, root)]

        while s:
            i, node = s.pop()
            if i == 0:
                s.append((1, node))
                if node.left:
                    s.append((0, node.left))
            elif i == 1:
                r.append(node.val)
                if node.right:
                    s.append((0, node.right))

        return r
