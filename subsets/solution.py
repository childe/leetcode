# -*- coding: utf-8 -*-

'''
https://leetcode-cn.com/problems/subsets/

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

'''


class Solution:
    def subsets(self, nums):
        stack = [([], nums)]
        ans = []

        while stack:
            # print(stack)
            c, ns = stack.pop()
            ans.append(c)
            for i, n in enumerate(ns):
                stack.append( (c+[n], ns[i+1:]) )

        return ans


def main():
    s = Solution()
    ans = s.subsets([1, 2, 3])
    print(ans)


if __name__ == '__main__':
    main()
