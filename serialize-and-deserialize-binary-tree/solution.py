# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Example: 

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
Clarification: The above format is the same as how LeetCode serializes a binary tree.
You do not necessarily need to follow this format,
so please be creative and come up with different approaches yourself.

Note: Do not use class member/global/static variables to store states.
Your serialize and deserialize algorithms should be stateless.
"""


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
        return ",".join(self.extend_to_list(root))

    def extend_to_list(self, root):
        # print(root.val if root else "null")
        if root is None:
            return ["null"]

        nodes = [str(root.val)]
        # print(nodes)
        nodes.extend(self.extend_to_list(root.left))
        # print(nodes)
        nodes.extend(self.extend_to_list(root.right))
        # print(nodes)
        return nodes

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        values = data.split(",")
        return self.deserializeR(values)[0]

    def deserializeR(self, values):
        """
        返回左子树, 和剩下的values(也就是右子树)
        """
        # print(values)
        if not values:
            return None, []
        if values[0] == "null":
            return None, values[1:]
        root = TreeNode(int(values[0]))
        l, remaining = self.deserializeR(values[1:])
        r, remaining = self.deserializeR(remaining)
        root.left = l
        root.right = r
        # print("==", root.val, l.val if l else "null", r.val if r else "null", remaining)
        return root, remaining


# Your Codec object will be instantiated and called as such:
def main():
    codec = Codec()
    root = TreeNode(1)
    # s = codec.serialize(root)
    # print(s)
    # new_root = codec.deserialize(s)
    # assert s == codec.serialize(new_root)

    root.left = TreeNode(2)
    s = codec.serialize(root)
    print("s", s)
    print()
    new_root = codec.deserialize(s)
    print()
    # print(new_root.val)
    # print(new_root.left.val)
    # print(new_root.right.val)
    new_s = codec.serialize(new_root)
    print("new_s", new_s)
    assert s == new_s

    root = TreeNode(1)
    s = codec.serialize(root)
    print(s)
    root.right = TreeNode(2)
    s = codec.serialize(root)
    new_root = codec.deserialize(s)
    new_s = codec.serialize(new_root)
    print(s)
    assert s == new_s


if __name__ == "__main__":
    main()
