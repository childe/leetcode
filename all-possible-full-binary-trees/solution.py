# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/all-possible-full-binary-trees/description/

A full binary tree is a binary tree where each node has exactly 0 or 2 children.

Return a list of all possible full binary trees with N nodes.  Each element of the answer is the root node of one possible tree.

Each node of each tree in the answer must have node.val = 0.

You may return the final list of trees in any order.

Input: 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]

1 <= N <= 20
"""

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
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
            for j in range(1, i, 2):
                for rootL in dp_arr[j]:
                    for rootR in dp_arr[i-j-1]:
                        new_root = TreeNode(0)
                        new_root.left = rootL
                        new_root.right = rootR
                        s.add(new_root)
            dp_arr[i] = s
        return list(dp_arr[N])


def main():
    s = Solution()
    for i in range(21):
        print len(s.allPossibleFBT(i))


if __name__ == '__main__':
    main()
