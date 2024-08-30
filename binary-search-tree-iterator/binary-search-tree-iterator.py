#!/usr/bin/env python3
"""
https://leetcode.cn/problems/binary-search-tree-iterator/description/
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.current = (
            TreeNode()
        )  # 刚初始化之后， current 其实是 head，next 时会依次前进

        if root is None:
            return

        tail = self.current

        def process(node):
            nonlocal tail
            tail.right = node
            tail = node

        st: list[tuple[int, TreeNode]] = [(0, root)]
        while st:
            flag, node = st.pop()
            if flag == 0:
                st.append((1, node))
                if node.left:
                    st.append((0, node.left))
            else:
                process(node)
                if node.right:
                    st.append((0, node.right))

    def next(self) -> int:
        r = self.current.right.val
        self.current = self.current.right
        return r

    def hasNext(self) -> bool:
        return self.current.right is not None
