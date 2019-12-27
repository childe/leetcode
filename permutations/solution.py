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
        if len(nums) == 1:
            return [nums]

        rst = []
        for i, n in enumerate(nums):
            for r in self.permute(nums[:i]+nums[i+1:]):
                rst.append([n]+r)
        return rst


def main():
    s = Solution()

    nums = [1, 2, 3]
    a = s.permute(nums)
    print(a)


if __name__ == '__main__':
    main()
