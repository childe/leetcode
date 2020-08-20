# -*- coding: utf-8 -*-
"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        rst = []

        rst.append([root.val])
        up_level_q, next_level_q = [root], []
        while up_level_q:
            level_nums = []
            for n in up_level_q:
                if n.left:
                    next_level_q.append(n.left)
                    level_nums.append(n.left.val)
                if n.right:
                    next_level_q.append(n.right)
                    level_nums.append(n.right.val)

            up_level_q = next_level_q
            next_level_q = []
            if level_nums:
                rst.append(level_nums)

        return rst


def main():
    s = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    rst = s.levelOrder(root)
    print(rst)


if __name__ == "__main__":
    main()
