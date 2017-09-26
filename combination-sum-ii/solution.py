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
    def combinationSum2Sorted(self, candidates, target):
        # print candidates, target
        if target == 0:
            return [()]
        if candidates == [] or target <= 0:
            return []
        if candidates[0] > target:
            return self.combinationSum2Sorted(candidates[1:], target)

        s = set()
        r1 = self.combinationSum2Sorted(candidates[1:], target)
        # print "r1", r1
        s.update(r1)
        r2 = self.combinationSum2Sorted(candidates[1:], target-candidates[0])
        # print "r2", r2
        s.update({(candidates[0],) + e for e in r2})

        return list({tuple(sorted(e)) for e in s})

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        >>> s = Solution()
        >>> s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
        [(1, 1, 6), (2, 6), (1, 2, 5), (1, 7)]
        >>> s.combinationSum2([1], 1)
        [(1,)]
        """
        candidates.sort()
        candidates.reverse()
        for i, e in enumerate(candidates):
            if e <= target:
                candidates = candidates[i:]
                break

        if candidates == []:
            return []

        return self.combinationSum2Sorted(candidates, target)


def f():
    s = Solution()
    s.combinationSum2([24,
                       31,
                       6,
                       19,
                       18,
                       30,
                       7,
                       33,
                       10,
                       10,
                       10,
                       15,
                       21,
                       33,
                       31,
                       10,
                       9,
                       15,
                       22,
                       6,
                       13,
                       11,
                       24,
                       17,
                       28,
                       33,
                       26,
                       9,
                       24,
                       11,
                       28,
                       14,
                       29,
                       29,
                       28,
                       12,
                       17,
                       22,
                       33,
                       14,
                       19,
                       8,
                       25,
                       27,
                       7,
                       13,
                       24,
                       33,
                       23,
                       12,
                       34,
                       24,
                       10,
                       23,
                       28,
                       25,
                       22],
                      26)


if __name__ == '__main__':
    import timeit
    print timeit.timeit("f()", setup="from __main__ import f", number=100)
    # s = Solution()
    # print s.combinationSum2([6, 5, 2, 1, 1], 8)
