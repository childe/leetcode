#!/usr/bin/env python3


"""
https://leetcode.cn/problems/find-duplicate-subtrees/

Given the root of a binary tree, return all duplicate subtrees.

For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with the same node values.

Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]

Input: root = [2,1,1]
Output: [[1]]

Input: root = [2,2,2,3,null,3,null]
Output: [[2,3],[3]]

Constraints:

The number of the nodes in the tree will be in the range [1, 10^4]
-200 <= Node.val <= 200
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode | None) -> list[TreeNode]:
        seen = {}
        uniq = set()
        ans = []
        idx = 1

        def postOrder(node: TreeNode | None) -> int:
            nonlocal idx, ans

            if node is None:
                return 0

            left = postOrder(node.left)
            right = postOrder(node.right)
            if got := seen.get((left, right, node.val)):
                if got not in uniq:
                    uniq.add(got)
                    ans.append(node)
                return got
            else:
                idx += 1
                seen[(left, right, node.val)] = idx
                return idx

        postOrder(root)
        return ans
