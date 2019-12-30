# -*- coding: utf-8 -*-

'''
https://leetcode-cn.com/problems/permutations-ii/

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''


class Solution(object):
    def _a_(self, nums):
        if len(nums) == 1:
            return [nums]

        rst = []
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i-1]:
                continue
            for r in self._a_(nums[:i]+nums[i+1:]):
                rst.append([n]+r)
        return rst

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        return self._a_(nums)


def main():
    s = Solution()

    nums = [1, 1, 2]
    a = s.permuteUnique(nums)
    print(a)
    assert a == [[1, 1, 2], [1, 2, 1], [2, 1, 1]]

    nums = [0, 1, 1, 2]
    a = s.permuteUnique(nums)
    print(a)
    assert a == [
        [
            0, 1, 1, 2], [
            0, 1, 2, 1], [
                0, 2, 1, 1], [
                    1, 0, 1, 2], [
                        1, 0, 2, 1], [
                            1, 1, 0, 2], [
                                1, 1, 2, 0], [
                                    1, 2, 0, 1], [
                                        1, 2, 1, 0], [
                                            2, 0, 1, 1], [
                                                2, 1, 0, 1], [
                                                    2, 1, 1, 0]]

    nums = [1, 2, 3]
    a = s.permuteUnique(nums)
    print(a)
    assert a == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]


if __name__ == '__main__':
    main()
