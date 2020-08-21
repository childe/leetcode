# -*- coding: utf-8 -*-


"""
https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        rst = [[root.val]]
        level_nodes = [root]
        # left_to_right = True

        while level_nodes:
            # if not left_to_right:
            # level_nodes.reverse()
            next_level_nodes = []
            values = []
            for n in level_nodes:
                if n.left:
                    next_level_nodes.append(n.left)
                    values.append(n.left.val)
                if n.right:
                    next_level_nodes.append(n.right)
                    values.append(n.right.val)
            if values:
                rst.append(values)
            level_nodes = next_level_nodes
            # left_to_right = not left_to_right

        for i, nums in enumerate(rst):
            if i % 2:
                rst[i].reverse()
        return rst


def main():
    s = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    rst = s.zigzagLevelOrder(root)
    print(rst)
    assert rst == [[3], [20, 9], [15, 7]]


if __name__ == "__main__":
    main()
