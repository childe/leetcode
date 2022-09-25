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

        cache = {}

        def f(x):
            return x * (x + 1) // 2

        def c(left, right):
            if (left, right) in cache:
                return cache[(left, right)]
            r = f(left + right + 1) - f(left) - f(right)
            cache[(left, right)] = r
            return r

        ans = 0

        """
        stack是一个单调栈，里面存的是 [num,pc]，pc 是指左边的被它挤压出来的数字个数。
        原始数组是[1,6,7,5,6,7,2,6,7], stack是[1,0],[6,0],[7,0] -> [1,0],[5,2] -> ...
        """
        stack = []
        for n in arr:
            # print(n,stack)
            pop_count = 0
            while stack and stack[-1][0] > n:
                v, pc = stack.pop()
                ans += c(pc, pop_count) * v
                pop_count += pc+1

            stack.append([n, pop_count])

        """
        [1,6,7,5,6,7,2,6,7] 最后的栈是 [(1,0),(2,5),(6,0),(7,0)]
        pop_count 是针对原始数组来说，累积的 pop 出来的个数，比如到 (2,5) 时，pop 出来了 2 个, (1,0)时，pop 出来了 8 个
        """
        pop_count = 0
        # print(stack)
        while stack:
            v, pc = stack.pop()
            ans += c(pc, pop_count) * v
            pop_count += pc + 1

        return ans % (10**9 + 7)
