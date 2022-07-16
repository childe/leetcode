#!/usr/bin/env python3
"""
https://leetcode.cn/problems/logical-or-of-two-binary-grids-represented-as-quad-trees/

Constraints:

quadTree1 and quadTree2 are both valid Quad-Trees each representing a n * n grid.
n == 2x where 0 <= x <= 9.
"""

# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val: int = val
        self.isLeaf: bool = isLeaf
        self.topLeft: None | Node = topLeft
        self.topRight: None | Node = topRight
        self.bottomLeft: None | Node = bottomLeft
        self.bottomRight: None | Node = bottomRight


class Solution:
    def intersect(self, q1: Node, q2: Node) -> Node:
        if q1.isLeaf:
            return q1 if q1.val == 1 else q2
        if q2.isLeaf:
            return q2 if q2.val == 1 else q1

        topLeft = self.intersect(q1.topLeft, q2.topLeft)
        topRight = self.intersect(q1.topRight, q2.topRight)
        bottomLeft = self.intersect(q1.bottomLeft, q2.bottomLeft)
        bottomRight = self.intersect(q1.bottomRight, q2.bottomRight)

        if (
            all([e.isLeaf for e in (topLeft, topRight, bottomLeft, bottomRight)])
            and len(set([e.val for e in (topLeft, topRight, bottomLeft, bottomRight)]))
            == 1
        ):
            node = Node(topLeft.val, True, None, None, None, None)
        else:
            node = Node(1, False, topLeft, topRight, bottomLeft, bottomRight)
        return node
