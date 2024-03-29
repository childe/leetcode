#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.cn/problems/can-i-win/

In the "100 game," two players take turns adding, to a running total, any integer from 1..10. The player who first causes the running total to reach or exceed 100 wins.

What if we change the game so that players cannot re-use integers?

For example, two players might take turns drawing from a common pool of numbers of 1..15 without replacement until they reach a total >= 100.

Given an integer maxChoosableInteger and another integer desiredTotal, determine if the first player to move can force a win, assuming both players play optimally.

You can always assume that maxChoosableInteger will not be larger than 20 and desiredTotal will not be larger than 300.

Example

Input:
maxChoosableInteger = 10
desiredTotal = 11

Output:
false

Explanation:
No matter which integer the first player choose, the first player will lose.
The first player can choose an integer from 1 up to 10.
If the first player choose 1, the second player can only choose integers from 2 up to 10.
The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
Same with other integers chosen by the first player, the second player will always win.
"""


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        """
        >>> s = Solution()
        >>> s.canIWin(10, 20)
        True
        >>> s.canIWin(10, 11)
        False
        >>> s.canIWin(10, 40)
        False
        >>> s.canIWin(4, 6)
        True
        >>> s.canIWin(18, 79)
        True
        >>> s.canIWin(20, 210)
        False
        >>> s.canIWin(20, 207)
        False
        >>> s.canIWin(19, 190)
        True
        """
        nums = list(range(1, maxChoosableInteger + 1))

        if desiredTotal <= 1:
            return True
        if sum(nums) < desiredTotal:
            return False
        if sum(nums) == desiredTotal:
            return maxChoosableInteger % 2 == 1

        def cache(c):
            def wrapper(f):
                def inner(nums, target):
                    if nums in c:
                        return c[nums]
                    r = f(nums, target)
                    # print(f"nums={bin(nums)} {target=} {r=}")
                    c[nums] = r
                    return r

                return inner

            return wrapper

        @cache({})
        def dfs(nums, target) -> bool:
            """
            nums = 0b10011 equals (5,2,1)
            """
            # print(f"nums={bin(nums)} {target=}")

            if (1 << (target - 1)) <= nums:
                return True

            if target <= 0:
                return True

            n = 0
            while (1 << n) <= nums:
                num = 1 << n
                # print(bin(num), bin(nums & (~num)), n + 1)
                if nums & num == 0:
                    n += 1
                    continue

                if not dfs(nums & (~num), target - (n + 1)):
                    return True

                n += 1

            return False

        return dfs(int("1" * maxChoosableInteger, 2), desiredTotal)


def main():
    s = Solution()
    print(s.canIWin(2, 2))


if __name__ == "__main__":
    main()
