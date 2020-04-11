# -*- coding: utf-8 -*-

'''
https://leetcode-cn.com/problems/permutation-sequence/

给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。

说明：

给定 n 的范围是 [1, 9]。
给定 k 的范围是[1,  n!]。
示例 1:

输入: n = 3, k = 3
输出: "213"
示例 2:

输入: n = 4, k = 9
输出: "2314"
'''


class Solution(object):
    def cache(fun):
        repo = {}

        def inner(*args):
            if args in repo:
                return repo[args]
            r = fun(*args)
            repo[args] = r
            return r
        return inner

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        r, i = self.needHowManyNums(k)
        l = list(range(1, n+1))
        return ''.join([str(e) for e in self.getPermutation2(l, k)])

    def getPermutation2(self, nums, k):
        # print(nums, k)

        if k == 1:
            return nums

        r, i = self.needHowManyNums(k)
        # print("!", r, i)
        if r == k:
            return nums[:-i]+nums[-i:][::-1]

        if i < len(nums):
            return nums[:-i]+self.getPermutation2(nums[-i:], k)

        rr = self.uniqCombineCount(i-1)
        d, m = k//rr, k % rr
        # print("!!", d, m)
        if m == 0:
            d -= 1
            rest = nums[:d]+nums[d+1:]
            return [nums[d]] + rest[::-1]

        return [nums[d]] + self.getPermutation2(
            nums[:d]+nums[d+1:], m)

    def needHowManyNums(self, k):
        for i in range(1, 1+k):
            r = self.uniqCombineCount(i)
            if r >= k:
                return r, i

    @cache
    def uniqCombineCount(self, n):
        r = 1
        for i in range(n):
            r *= (n-i)
        return r


def main():
    s = Solution()
    assert(1 == s.uniqCombineCount(1))
    assert(6 == s.uniqCombineCount(3))
    assert(2 == s.uniqCombineCount(2))

    assert((1, 1) == s.needHowManyNums(1))
    assert((6, 3) == s.needHowManyNums(3))
    assert((6, 3) == s.needHowManyNums(6))
    assert((24, 4) == s.needHowManyNums(7))

    ans = s.getPermutation2([3], 1)
    assert(ans == [3])

    ans = s.getPermutation2([1, 3], 1)
    assert([1, 3] == ans)

    ans = s.getPermutation(3, 1)
    print(ans)
    assert(ans == '123')

    ans = s.getPermutation(3, 2)
    assert(ans == '132')

    ans = s.getPermutation(3, 4)
    assert(ans == '231')

    ans = s.getPermutation(3, 6)
    assert(ans == '321')

    ans = s.getPermutation(9, 1)
    print(ans)
    assert(ans == '123456789')

    ans = s.getPermutation(9, 3)
    print(ans)
    assert(ans == '123456879')

    ans = s.getPermutation(4, 3)
    print(ans)
    assert(ans == '1324')

    ans = s.getPermutation(4, 9)
    assert(ans == '2314')

    ans = s.getPermutation(9, 362879)
    print(ans)
    assert(ans == '987654312')

    ans = s.getPermutation(9, 362880)
    print(ans)
    assert(ans == '987654321')

    ans = s.getPermutation(8, 31492)
    print(ans)
    assert(ans == '72641583')


if __name__ == '__main__':
    main()
