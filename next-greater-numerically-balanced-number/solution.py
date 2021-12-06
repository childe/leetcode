# -*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/next-greater-numerically-balanced-number/

An integer x is numerically balanced if for every digit d in the number x, there are exactly d occurrences of that digit in x.

Given an integer n, return the smallest numerically balanced number strictly greater than n.

 

Example 1:

Input: n = 1
Output: 22
Explanation: 
22 is numerically balanced since:
- The digit 2 occurs 2 times. 
It is also the smallest numerically balanced number strictly greater than 1.
Example 2:

Input: n = 1000
Output: 1333
Explanation: 
1333 is numerically balanced since:
- The digit 1 occurs 1 time.
- The digit 3 occurs 3 times. 
It is also the smallest numerically balanced number strictly greater than 1000.
Note that 1022 cannot be the answer because 0 appeared more than 0 times.
Example 3:

Input: n = 3000
Output: 3133
Explanation: 
3133 is numerically balanced since:
- The digit 1 occurs 1 time.
- The digit 3 occurs 3 times.
It is also the smallest numerically balanced number strictly greater than 3000.
 

Constraints:

0 <= n <= 10^6
"""


class Solution:
    def combineToNumbers(self, nums: [str]) -> {str}:
        """
        >>> s = Solution()
        >>> s.combineToNumbers(["1","2","2"])
        {"122", "212", "221"}
        """
        if len(nums) == 1:
            return set(nums)

        rst = set()
        f = nums[0]
        for s in self.combineToNumbers(nums[1:]):
            for i in range(0, len(s)):
                rst.add(s[:i] + f + s[i:])
            rst.add(s + f)

        return rst

    def combines(self, n):
        """
        >>> s = Solution()
        >>> s.combines(5)
        [(2, 3), (1, 4), (5,)]
        >>> s.combines(6)
        [(6,), (2, 4), (1, 2, 3), (1, 5)]
        """
        if n == 1 or n == 2:
            return [(n,)]

        rst = []
        for i in range(1, (1 + n) // 2):
            for r in self.combines(n - i):
                rst.append((i,) + r)

        rst.append((n,))

        return list(set([tuple(sorted(e)) for e in rst if len(e) == len(set(e))]))

    def allBeautifulNumber(self, l: int) -> int:
        candidates = []
        for combile in self.combines(l):
            # print(combile)
            nums = []
            for c in combile:
                nums.extend(str(c) * c)
            # print(nums)
            candidates.extend([int(e) for e in self.combineToNumbers(nums)])
        return candidates

    def nextBeautifulNumber(self, n: int) -> int:
        l = len(str(n))

        for r in sorted(self.allBeautifulNumber(l)):
            # print(r)
            if r > n:
                return r

        l += 1
        for r in sorted(self.allBeautifulNumber(l)):
            # print(r)
            if r > n:
                return r


def main():
    s = Solution()

    # output = s.combineToNumbers(["1", "2", "2"])
    # print(output)
    # output = s.combineToNumbers(["1", "2"])
    # print(output)
    # output = s.combineToNumbers(["3", "3", "3"])
    # print(output)
    # output = s.combineToNumbers(["1", "3", "3", "3"])
    # print(output)
    # output = s.combineToNumbers(["1", "2", "2", "3", "3", "3"])
    # print(output)

    # for n in range(1, 10):
    # output = s.combines(n)
    # print(n, output)

    tables = [
        (1, 22),
        (1000, 1333),
        (3000, 3133),
        (109999, 122333),
        (59866, 122333),
    ]

    for n, ans in tables:
        output = s.nextBeautifulNumber(n)
        print(n, ans, output)
        assert output == ans


if __name__ == "__main__":
    main()
