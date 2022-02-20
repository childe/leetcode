#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/number-of-ways-to-reconstruct-a-tree/

1719. Number Of Ways To Reconstruct A Tree

*Hard*

You are given an array pairs, where pairs[i] = [xi, yi], and:

There are no duplicates.
xi < yi
Let ways be the number of rooted trees that satisfy the following conditions:

The tree consists of nodes whose values appeared in pairs.
A pair [xi, yi] exists in pairs if and only if xi is an ancestor of yi or yi is an ancestor of xi.
Note: the tree does not have to be a binary tree.
Two ways are considered to be different if there is at least one node that has different parents in both ways.

Return:

0 if ways == 0
1 if ways == 1
2 if ways > 1
A rooted tree is a tree that has a single root node, and all edges are oriented to be outgoing from the root.

An ancestor of a node is any node on the path from the root to that node (excluding the node itself). The root has no ancestors.

 

Example 1:


Input: pairs = [[1,2],[2,3]]
Output: 1
Explanation: There is exactly one valid rooted tree, which is shown in the above figure.
Example 2:


Input: pairs = [[1,2],[2,3],[1,3]]
Output: 2
Explanation: There are multiple valid rooted trees. Three of them are shown in the above figures.
Example 3:

Input: pairs = [[1,2],[2,3],[2,4],[1,5]]
Output: 0
Explanation: There are no valid rooted trees.
 

Constraints:

1 <= pairs.length <= 10^5
1 <= xi < yi <= 500
The elements in pairs are unique.
"""


class Solution:
    def checkWays(self, pairs: list[list[int]]) -> int:
        """
        >>> s = Solution()
        >>> s.checkWays([[1,2],[2,3]])
        1
        >>> s.checkWays([[1,2],[2,3],[1,3]])
        2
        >>> s.checkWays([[1,2],[2,3],[2,4],[1,5]])
        0
        >>> s.checkWays([[5,7],[11,12],[2,9],[8,10],[1,4],[3,6]])
        0
        """
        degrees = [0] * 501
        adjs = [set() for _ in range(501)]
        all_set = set()

        for i, j in pairs:
            adjs[i].add(i)
            adjs[i].add(j)

            adjs[j].add(i)
            adjs[j].add(j)

            degrees[i] += 1
            degrees[j] += 1

            all_set.add(i)
            all_set.add(j)

        max_degree = max(degrees)
        # print(f"{max_degree=}")
        # if degrees.count(max_degree) > 1:
        # return 0

        if max_degree != len(all_set) - 1:
            return 0

        ans = 1

        for i, j in pairs:
            # print(i, j)
            # print(degrees[i], degrees[j])
            # print(adjs[i], adjs[j])
            if degrees[i] == degrees[j]:
                if adjs[i] != adjs[j]:
                    return 0
                ans = 2
            elif degrees[i] > degrees[j]:
                if not adjs[i].issuperset(adjs[j]):
                    return 0
            else:
                if not adjs[j].issuperset(adjs[i]):
                    return 0

        return ans
