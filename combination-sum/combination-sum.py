#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/combination-sum/description/

Given a set of candidate numbers (C) (without duplicates) and a target number (T),
find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:
[
  [7],
  [2, 2, 3]
]
"""


class Solution(object):
    def combinationSumSorted(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: Set(List[int])
        >>> s = Solution()
        >>> s.combinationSum([2, 3, 6, 7], 7)
        set([(7,), (2, 2, 3)])
        """
        if target < candidates[0]:
            return set()
        if target == candidates[0]:
            return {(target, )}

        s = set()
        r1 = self.combinationSum(candidates[1:], target)
        s.update(r1)

        r2 = {(candidates[0],) + e for e in self.combinationSum(candidates, target-candidates[0])}
        s.update(r2)

        return s

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: Set(List[int])
        >>> s = Solution()
        >>> s.combinationSum([2, 3, 6, 7], 7)
        set([(7,), (2, 2, 3)])
        >>> s.combinationSum([], 7)
        set([])
        """
        if candidates == []:
            return set()
        candidates.sort()
        return list(self.combinationSumSorted(candidates, target))
