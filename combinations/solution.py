# -*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/combinations/

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

"""


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return self.combineNums(list(range(1, n+1)), k)

    def combineNums(self, nums, k):
        # print(nums, k)
        if not nums:
            return []
        if k == 1:
            return [[n] for n in nums]

        r = []
        first = nums[0]
        r.extend([[first]+e for e in self.combineNums(nums[1:], k-1)])
        r.extend(self.combineNums(nums[1:], k))
        return r


def main():
    s = Solution()
    n = 4
    k = 2
    ans = s.combine(n, k)
    print(ans)
    assert sorted(ans) == sorted([
        [2, 4],
        [3, 4],
        [2, 3],
        [1, 2],
        [1, 3],
        [1, 4],
        ])


if __name__ == '__main__':
    main()
