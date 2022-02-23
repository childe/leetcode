#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/problems/the-number-of-good-subsets/

1994. The Number of Good Subsets
You are given an integer array nums. We call a subset of nums good if its product can be represented as a product of one or more distinct prime numbers.

For example, if nums = [1, 2, 3, 4]:
[2, 3], [1, 2, 3], and [1, 3] are good subsets with products 6 = 2*3, 6 = 2*3, and 3 = 3 respectively.
[1, 4] and [4] are not good subsets with products 4 = 2*2 and 4 = 2*2 respectively.
Return the number of different good subsets in nums modulo 10^9 + 7.

A subset of nums is any array that can be obtained by deleting some (possibly none or all) elements from nums. Two subsets are different if and only if the chosen indices to delete are different.

 

Example 1:

Input: nums = [1,2,3,4]
Output: 6
Explanation: The good subsets are:
- [1,2]: product is 2, which is the product of distinct prime 2.
- [1,2,3]: product is 6, which is the product of distinct primes 2 and 3.
- [1,3]: product is 3, which is the product of distinct prime 3.
- [2]: product is 2, which is the product of distinct prime 2.
- [2,3]: product is 6, which is the product of distinct primes 2 and 3.
- [3]: product is 3, which is the product of distinct prime 3.

Example 2:

Input: nums = [4,2,3,15]
Output: 5
Explanation: The good subsets are:
- [2]: product is 2, which is the product of distinct prime 2.
- [2,3]: product is 6, which is the product of distinct primes 2 and 3.
- [2,15]: product is 30, which is the product of distinct primes 2, 3, and 5.
- [3]: product is 3, which is the product of distinct prime 3.
- [15]: product is 15, which is the product of distinct primes 3 and 5.
 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 30
"""

from collections import Counter


class Solution:
    def numberOfGoodSubsets(self, nums: list[int]) -> int:
        """
        >>> s = Solution()
        >>> s.numberOfGoodSubsets([1,1,2,3])
        12
        >>> s.numberOfGoodSubsets([1,2,3,4])
        6
        >>> s.numberOfGoodSubsets([4,2,3,15])
        5
        >>> s.numberOfGoodSubsets([1,1,1,1])
        0
        >>> s.numberOfGoodSubsets([12,3])
        1
        >>> s.numberOfGoodSubsets([18,28,2,17,29,30,15,9,12])
        19
        >>> s.numberOfGoodSubsets([6,8,1,8,6,5,6,11,17])
        62
        >>> s.numberOfGoodSubsets([5,10,1,26,24,21,24,23,11,12,27,4,17,16,2,6,1,1,6,8,13,30,24,20,2,19])
        5368
        """
        m = {
            1: set([1]),
            2: set([2]),
            3: set([3]),
            5: set([5]),
            6: set([2, 3]),
            7: set([7]),
            10: set([2, 5]),
            11: set([11]),
            13: set([13]),
            14: set([2, 7]),
            15: set([3, 5]),
            17: set([17]),
            19: set([19]),
            21: set([3, 7]),
            22: set([2, 11]),
            23: set([23]),
            26: set([2, 13]),
            29: set([29]),
            30: set([2, 3, 5]),
        }

        existed = []
        sorted_nums = sorted(list(set(nums)))
        if 1 in sorted_nums:
            sorted_nums.remove(1)
        for n in sorted_nums:
            if n not in m:
                continue
            s = m[n]
            new_existed = [([n], s)]
            # print(f"n={n}, s={s}")
            for origin, prime_nums in existed:
                if not s.intersection(prime_nums):
                    new_existed.append((origin + [n], prime_nums.union(s)))
            existed += new_existed

        origin = [e[0] for e in existed]
        # print(f"{origin=}")
        # print(f"{len(origin)=}")

        ans, c = 0, Counter(nums)
        for e, _ in existed:
            s = 1
            for n in e:
                s *= c[n]
            ans += s

        c = nums.count(1)
        ans *= 1 << c
        return ans % (10**9 + 7)
