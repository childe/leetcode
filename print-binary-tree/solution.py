#!/usr/bin/env python3

"""
https://leetcode.cn/problems/print-binary-tree/

Given the root of a binary tree, construct a 0-indexed m x n string matrix res that represents a formatted layout of the tree. The formatted layout matrix should be constructed using the following rules:

The height of the tree is height and the number of rows m should be equal to height + 1.
The number of columns n should be equal to 2^(height+1) - 1.
Place the root node in the middle of the top row (more formally, at location res[0][(n-1)/2]).
For each node that has been placed in the matrix at position res[r][c], place its left child at res[r+1][c-2height-r-1] and its right child at res[r+1][c+2height-r-1].
Continue this process until all the nodes in the tree have been placed.
Any empty cells should contain the empty string "".
Return the constructed matrix res.

 

Example 1:


Input: root = [1,2]
Output: 
[["","1",""],
 ["2","",""]]
Example 2:


Input: root = [1,2,3,null,4]
Output: 
[["","","","1","","",""],
 ["","2","","","","3",""],
 ["","","4","","","",""]]
 

Constraints:

The number of nodes in the tree is in the range [1, 2^10].
-99 <= Node.val <= 99
The depth of the tree will be in the range [1, 10].
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def height(self, root: TreeNode) -> int:
        """
        >>> s = Solution()
        >>> root = TreeNode(1)
        >>> root.left = TreeNode(2)
        >>> s.height(root)
        1
        >>> s.height(root.left)
        0
        """
        left_height, right_height = 0, 0
        if root.left is None and root.right is None:
            return 0

        if root.left is not None:
            left_height = self.height(root.left)
        if root.right is not None:
            right_height = self.height(root.right)

        return max(left_height, right_height) + 1

    def printTree(self, root: TreeNode | None) -> list[list[str]]:
        """
        >>> s = Solution()
        >>> root = TreeNode(1)
        >>> root.left = TreeNode(2)
        >>> s.printTree(root)
        [['', 1, ''], [2, '', '']]
        """
        if root is None:
            return []

        height = self.height(root)
        rst = []
        col_count = 2 ** (height + 1) - 1
        for i in range(height+1):
            rst.append([""] * col_count)

        def putNode(node: TreeNode, height: int, left: int, right: int):
            p = (left + right) // 2
            rst[height][p] = str(node.val)
            if node.left:
                putNode(node.left, height + 1, left, p)
            if node.right:
                putNode(node.right, height + 1, p, right)

        putNode(root, height=0, left=0, right=col_count)
        return rst
