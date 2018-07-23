# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/serialize-and-deserialize-bst/description/


Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
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


# Your Codec object will be instantiated and called as such:
def main():
    codec = Codec()
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    s = codec.serialize(root)
    print s

    root = codec.deserialize(s)
    print codec.serialize(root)

if __name__ == '__main__':
    main()
