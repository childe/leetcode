#!/usr/bin/env python


"""
https://leetcode.cn/problems/sum-of-subarray-minimums/

给定一个整数数组 arr，找到 min(b) 的总和，其中 b 的范围为 arr 的每个（连续）子数组。

由于答案可能很大，因此 返回答案模 10^9 + 7 。

 

示例 1：

输入：arr = [3,1,2,4]
输出：17
解释：
子数组为 [3]，[1]，[2]，[4]，[3,1]，[1,2]，[2,4]，[3,1,2]，[1,2,4]，[3,1,2,4]。 
最小值为 3，1，2，4，1，1，2，1，1，1，和为 17。
示例 2：

输入：arr = [11,81,94,43,3]
输出：444
 

提示：

1 <= arr.length <= 3 * 10^4
1 <= arr[i] <= 3 * 10^4
"""


class MinStack(object):
    def __init__(self):
        self.s = []
        self.minS = []

    def push(self, x):
        self.s.append(x)
        if not self.minS or x <= self.minS[-1]:
            self.minS.append(x)

    def pop(self):
        if self.s[-1] == self.minS[-1]:
            self.minS = self.minS[:-1]

        r = self.s[-1]
        self.s = self.s[:-1]
        return r

    def min(self):
        return self.minS[-1]


class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        """
        >>> s = Solution()
        >>> s.sumSubarrayMins([3,1,2,4])
        17
        >>> s.sumSubarrayMins([11,81,94,43,3])
        444
        """
        s = 0

        arr.sort()

        cache = {}

        def c(n, i):
            if i == 0:
                return 1
            if n < i:
                return 0
            if (n, i) in cache:
                return cache[(n, i)]
            r = n * c(n - 1, i - 1) // i
            cache[(n, i)] = r
            return r

        for i, n in enumerate(arr):
            print(f"{i=} {n=}")
            current_len = len(arr) - i
            for j in range(1, current_len + 1):
                s += (c(current_len, j) - c(current_len - 1, j)) * n
                print(f"{j=} {current_len=} {s=}")

            print(f"=== {s=} {i=} {n=}")

        return s


s = Solution()
r = s.sumSubarrayMins([1, 2, 3, 4])
print(r)
