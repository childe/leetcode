#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/combination-sum-ii/description/

Given a collection of candidate numbers (C) and a target number (T),
find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
"""


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        >>> s = Solution()
        >>> s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
        [(2, 6), (1, 1, 6), (1, 2, 5), (1, 7)]
        >>> s.combinationSum2([1], 1)
        [(1,)]
        """
        candidates.sort()
        for i, e in enumerate(candidates):
            if e > target:
                candidates = candidates[:i]
                break

        if candidates == []:
            return []

        candidates.reverse()

        rst = set()
        stack = [((), 0, target)]  # (pre parts, start, target)
        while stack:
            # print stack
            pre_parts, start, target = stack.pop()
            # print pre_parts, start, target, candidates[start:]
            if target == 0:
                rst.add(pre_parts)
                continue
            if start >= len(candidates):
                continue
            if target < 0:
                continue
            stack.append((pre_parts, start+1, target))
            stack.append((pre_parts+(candidates[start],), start+1, target-candidates[start]))

        return list(rst)


def f():
    s = Solution()
    s.combinationSum2([13,
                       23,
                       25,
                       11,
                       7,
                       26,
                       14,
                       11,
                       27,
                       27,
                       26,
                       12,
                       8,
                       20,
                       22,
                       34,
                       27,
                       17,
                       5,
                       26,
                       31,
                       11,
                       16,
                       27,
                       13,
                       20,
                       29,
                       18,
                       7,
                       14,
                       13,
                       15,
                       25,
                       25,
                       21,
                       27,
                       16,
                       22,
                       33,
                       8,
                       15,
                       25,
                       16,
                       18,
                       10,
                       25,
                       9,
                       24,
                       7,
                       32,
                       15,
                       26,
                       30,
                       19],
                      25)


if __name__ == '__main__':
    import timeit
    print timeit.timeit("f()", setup="from __main__ import f", number=100)
    # s = Solution()
    # print s.combinationSum2([6, 5, 2, 1, 1], 8)
