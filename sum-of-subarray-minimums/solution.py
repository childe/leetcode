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
            self.minS.pop()

        return self.s.pop()

    def top(self):
        return self.s[-1]

    def getMin(self):
        return self.minS[-1]


class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        """
        >>> s = Solution()
        >>> s.sumSubarrayMins([3,1,2,4])
        17
        >>> s.sumSubarrayMins([11,81,94,43,3])
        444
        >>> s.sumSubarrayMins([1,1,1,2])
        11
        """
        s = 0

        for i, n in enumerate(arr):
            subArr = arr[i:]
            minStack = MinStack()
            for n in subArr:
                minStack.push(n)
            while minStack.s:
                s += minStack.getMin()
                minStack.pop()

        return s % (10**9 + 7)
