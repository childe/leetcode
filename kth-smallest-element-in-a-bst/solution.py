# -*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst/

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

 

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1

Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

 

Constraints:

The number of elements of the BST is between 1 to 10^4.
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not self.nodeCountCache:
            self.nodeCountCache
        leftCount = self.nodeCount(root.left)
        if leftCount == k - 1:
            return root.val
        if leftCount < k - 1:
            return self.kthSmallest(root.right, k - leftCount - 1)
        return self.kthSmallest(root.left, k)

    def nodeCount(self, root):
        if root in self.nodeCountCache:
            return self.nodeCountCache[root]
        if root is None:
            return 0
        r = self.nodeCount(root.left) + self.nodeCount(root.right) + 1
        self.nodeCountCache[root] = r
        return r
