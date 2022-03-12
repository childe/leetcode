#!/usr/bin/env python3

"""
https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal/

Given the root of an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)



Example 1:


Input: root = [1,null,3,2,4,null,5,6]
Output: [5,6,3,2,4,1]
Example 2:


Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]


Constraints:

The number of nodes in the tree is in the range [0, 10^4].
0 <= Node.val <= 10^4
The height of the n-ary tree is less than or equal to 1000.


Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: "Node") -> list[int]:
        """
        >>> s = Solution()
        >>> s.postorder(s.gen_tree([1, None, 3, 2, 4, None, 5, 6]))
        [5, 6, 3, 2, 4, 1]
        >>> s.postorder(s.gen_tree([1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10, None, None, 11, None, 12, None, 13, None, None, 14]))
        [2, 6, 14, 11, 7, 3, 12, 8, 4, 13, 9, 10, 5, 1]
        """
        ans = []
        s: list[tuple["Node", int]] = [(root, 0)]
        while s:
            node, count = s.pop()
            if count == 1:
                ans.append(node.val)
            else:
                s.append((node, 1))
                for child in node.children[::-1]:
                    s.append((child, 0))

        return ans

    def gen_tree(self, nodes):
        root = Node(nodes[0], [])
        candidate_list = [root]
        current = root
        for e in nodes[1:]:
            if e is None:
                current = candidate_list.pop()
            else:
                node = Node(e, [])
                candidate_list.insert(0, node)
                current.children.append(node)

        return root
