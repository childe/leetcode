#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
https://leetcode.cn/problems/product-of-array-except-self/description/
"""


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        if not nums:
            return []
        if len(nums) == 1:
            return [0]

        ans = [1] * len(nums)
        for i in range(1, len(nums)):
            ans[i] = ans[i - 1] * nums[i - 1]

        r = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            ans[i] = ans[i] * r
            r *= nums[i]

        return ans


def main():
    s = Solution()
    print(s.productExceptSelf([1, 2, 3, 4]))
    print(s.productExceptSelf([-1, 1, 0, -3, 3]))
    print(s.productExceptSelf([1]))
    print(s.productExceptSelf([1, 2]))
    print(s.productExceptSelf([]))
    print(s.productExceptSelf([4, 3, 2, 1, 2]))
    print(s.productExceptSelf([2, 3, 4, 5]))


if __name__ == "__main__":
    main()
