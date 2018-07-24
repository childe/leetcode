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
            return ""
        q = list()
        q.append(root)
        serialized_strs = list()
        while q:
            t = q.pop()
            if t:
                serialized_strs.append(str(t.val))
                q.append(t.left)
                q.append(t.right)
            else:
                serialized_strs.append("#")
        return " ".join(serialized_strs)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        vals = data.split(" ")
        # print vals
        root = TreeNode(vals[0])
        stack = [(root, 0)]  # 0: no left, no right; 1 has right, no left 2; has right has left
        for val in vals[1:]:
            node, flag = stack.pop()

            if val == '#':
                n = None
            else:
                n = TreeNode(int(val))

            if flag == 0:
                node.right = n
                stack.append((node, 1))
            elif flag == 1:
                node.left = n

            if n is not None:
                stack.append((n, 0))

        return root

# Your Codec object will be instantiated and called as such:


def main():
    codec = Codec()
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)
    root.right = TreeNode(7)
    root.right.left = TreeNode(6)
    s = codec.serialize(root)
    print s

    root = codec.deserialize(s)
    print codec.serialize(root)


if __name__ == '__main__':
    main()
