# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/description/

Return any binary tree that matches the given preorder and postorder traversals.

Values in the traversals pre and post are distinct positive integers.



Example 1:

Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]


Note:

1 <= pre.length == post.length <= 30
pre[] and post[] are both permutations of 1, 2, ..., pre.length.
It is guaranteed an answer exists. If there exists multiple answers, you can return any of them.
"""

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def serializeTree(root):
    """
    :type root: TreeNode
    :rtype: list[int]
    """
    if root is None:
        return []

    r = []
    s = [root]
    while s:
        n = s.pop()
        r.append(n.val)
        if n.left:
            s.insert(0, n.left)
        if n.right:
            s.insert(0, n.right)
    return r


class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        print pre, post
        if len(pre) != len(post):
            return None

        if pre == []:
            return None

        if pre[0] != post[-1]:
            return None

        if len(pre) == 1:
            return TreeNode(pre[0])

        root = TreeNode(pre[0])
        for i, n in enumerate(post):
            if n == pre[1]:
                left = self.constructFromPrePost(pre[1:i+2], post[:i+1])
                right = self.constructFromPrePost(pre[i+2:], post[i+1:-1])
                root.left, root.right = left, right
                return root


if __name__ == '__main__':
    s = Solution()
    # print serializeTree(s.constructFromPrePost(pre=[1, 2, 4, 5, 3, 6, 7], post=[4, 5, 2, 6, 7, 3, 1]))
    print serializeTree(s.constructFromPrePost(pre=[1, 2], post=[2, 1]))
