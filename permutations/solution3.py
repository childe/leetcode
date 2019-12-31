# -*- coding: utf-8 -*-

'''
https://leetcode-cn.com/problems/permutations/

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
'''


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return (lambda: lambda n: (lambda f,n:f(f,n))(lambda f,ns:[e for sub in [(lambda n, ns:[[n]+r for r in f(f,ns)])(n, ns[:i]+ns[i+1:]) for i, n in enumerate(ns)] for e in sub]  if len(ns) > 1 else [ns],n))()(nums)

s = Solution()
a = s.permute([1,2,3])
print(a)
