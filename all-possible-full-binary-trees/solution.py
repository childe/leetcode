# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/all-possible-full-binary-trees/description/

A full binary tree is a binary tree where each node has exactly 0 or 2 children.

Return a list of all possible full binary trees with N nodes.  Each element of the answer is the root node of one possible tree.

Each node of each tree in the answer must have node.val = 0.

You may return the final list of trees in any order.

Input: 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
"""

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def serialize(self, root):
        """
        :type root: TreeNode
        :rtype: list[int]
        >>> s = Solution()
        >>> n = TreeNode(0)
        >>> s.serialize(n)
        '0,,'
        >>> n.left = TreeNode(0)
        >>> n.left.left = TreeNode(0)
        >>> n.left.right = TreeNode(0)
        >>> s.serialize(n)
        '0,0,,0,0,,,,'
        >>> n.right = TreeNode(0)
        >>> s.serialize(n)
        '0,0,0,0,0,,,,,,'
        """
        rst = []
        s = [root]
        while s:
            n = s.pop()
            if n is None:
                rst.append('')
                continue
            rst.append('0')
            s.insert(0, n.left)
            s.insert(0, n.right)

        return ','.join(rst)

    def add2NodesToTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode, TreeNode
        """
        a = TreeNode(0)
        a.left = root
        a.right = TreeNode(0)

        b = TreeNode(0)
        b.right = root
        b.left = TreeNode(0)

        return a, b

    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if N == 1:
            return [TreeNode(0)]
        if N % 2 == 0:
            return []

        s = set()
        s.add(TreeNode(0))

        dp_arr = {1: s}

        for i in range(3, 1+N, 2):
            s = set()
            serializedTree = set()
            for j in range(1, i, 2):
                for rootL in dp_arr[j]:
                    for rootR in dp_arr[i-j-1]:
                        new_root = TreeNode(0)
                        new_root.left = rootL
                        new_root.right = rootR
                        if new_root not in serializedTree:
                            serializedTree.add(new_root)
                            s.add(new_root)
            dp_arr[i] = s
        return list(dp_arr[N])


def main():
    s = Solution()
    for root in s.allPossibleFBT(21):
        print s.serialize(root)


if __name__ == '__main__':
    main()
