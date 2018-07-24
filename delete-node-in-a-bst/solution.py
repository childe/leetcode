# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/delete-node-in-a-bst/description/

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Note: Time complexity should be O(height of tree).

Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7
"""

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return u'{}'

        l = self.serialize(root.left)
        r = self.serialize(root.right)
        return u'{}{}:[{},{}]{}'.format('{', root.val, l, r, '}')

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '{}':
            return None

        val, i, l = None, 0, len(data)
        for i in range(1, l):
            if data[i] == ':':
                val = int(data[1:i])
                break
        node = TreeNode(val)

        o, leftBracketCount = i+2, 0
        for i in range(i+2, l):  # starts with {
            if data[i] == '{':
                leftBracketCount += 1
            if data[i] == '}':
                leftBracketCount -= 1
                if leftBracketCount == 0:
                    node.left = self.deserialize(data[o:i+1])
                    break
        node.right = self.deserialize(data[i+2:-2])
        return node


class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        # find key
        rootP = TreeNode(None)
        rootP.left = root
        p, f, c = rootP, 0, root
        while c:
            if c.val == key:
                break
            if c.val < key:
                p, f = c, 1  # p.right is c
                c = c.right
            else:
                p, f = c, 0  # p.left is c
                c = c.left

        # if p:
            # print 'p', p.val
        # if c:
            # print 'c', c.val

        if c is None:
            return rootP.left

        if c.left is None:
            if f == 0:
                p.left = c.right
            else:
                p.right = c.right
            return rootP.left

        if c.right is None:
            if f == 0:
                p.left = c.left
            else:
                p.right = c.left
            return rootP.left

        mostLeftP, mostLeft = c, c.right
        while mostLeft.left:
            mostLeftP, mostLeft = mostLeft, mostLeft.left
        # print 'mostLeftP', mostLeftP.val
        # print 'mostLeft', mostLeft.val

        if f == 0:
            p.left = mostLeft
        else:
            p.right = mostLeft

        mostLeft.left = c.left
        if mostLeft is not c.right:
            mostLeftP.left = mostLeft.right
            mostLeft.right = c.right

        return rootP.left


import unittest
class TestSolution(unittest.TestCase):

    def test_findMedianSortedArrays(self):
        s = Solution()
        c = Codec()
        root = c.deserialize('{5:[{3:[{2:[{},{}]},{4:[{},{}]}]},{}]}')
        root = s.deleteNode(root, 2)
        self.assertEqual(u'{5:[{3:[{},{4:[{},{}]}]},{}]}', c.serialize(root))

        root = c.deserialize('{5:[{3:[{2:[{},{}]},{4:[{},{}]}]},{}]}')
        root = s.deleteNode(root, 4)
        self.assertEqual(u'{5:[{3:[{2:[{},{}]},{}]},{}]}', c.serialize(root))

        root = c.deserialize('{5:[{3:[{2:[{},{}]},{4:[{},{}]}]},{}]}')
        root = s.deleteNode(root, 3)
        self.assertEqual(u'{5:[{4:[{2:[{},{}]},{}]},{}]}', c.serialize(root))

        root = c.deserialize('{5:[{3:[{2:[{},{}]},{4:[{},{}]}]},{}]}')
        root = s.deleteNode(root, 5)
        self.assertEqual(u'{3:[{2:[{},{}]},{4:[{},{}]}]}', c.serialize(root))

        root = c.deserialize('{7:[{3:[{2:[{},{}]},{6:[{5:[{},{}]},{}]}]},{}]}')
        root = s.deleteNode(root, 3)
        self.assertEqual(u'{7:[{5:[{2:[{},{}]},{6:[{},{}]}]},{}]}', c.serialize(root))


if __name__ == '__main__':
    unittest.main()
    # s = Solution()
    # c = Codec()
    # root = c.deserialize('{7:[{3:[{2:[{},{}]},{6:[{5:[{},{}]},{}]}]},{}]}')
    # print c.serialize(root)
    # root = s.deleteNode(root, 3)
    # print c.serialize(root)
