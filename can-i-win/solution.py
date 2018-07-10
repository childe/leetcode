#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/can-i-win/description/

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


class Solution(object):
    def canWin2(self, myPool, rivalPool, total):
        """
        >>> s = Solution()
        >>> s.canWin2([1,3], [2,4], 10)
        False
        >>> s.canWin2([1], [2], 7)
        True
        """
        # print myPool, rivalPool, total
        safeA = [None] * total
        safeB = [None] * total
        for n in range(1, total):
            if n <= max(rivalPool):
                safeA[n] = False
                continue
            if n <= max(myPool):
                safeB[n] = False
                continue
            safeA[n] = not any(safeB[n-i] for i in myPool if n-i > 0)
            safeB[n] = not any(safeA[n-i] for i in rivalPool if n-i > 0)

        return any(safeA[-max(myPool):])

    def canWin(self, myPool, rivalPool, restPool, total):
        # print myPool, rivalPool, restPool, total
        if total <= max(myPool+restPool):
            return True

        if restPool == []:
            return self.canWin2(myPool, rivalPool, total)

        for i, e in enumerate(restPool):
            if not self.canWin(rivalPool, myPool+[e], restPool[:i]+restPool[i+1:], total-e):
                return True

        for i, e in enumerate(myPool):
            if not self.canWin(rivalPool, myPool, restPool, total-e):
                return True

        return False

    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        >>> s = Solution()
        >>> s.canIWin(2, 10)
        True
        >>> s.canIWin(10, 20)
        True
        >>> s.canIWin(10, 11)
        False
        >>> s.canIWin(10, 40)
        False
        >>> s.canIWin(4, 6)
        True
        """
        return self.canWin([], [], range(1, 1+maxChoosableInteger), desiredTotal)


def main():
    s = Solution()
    # print s.canWin([], [], range(1, 11), 40)

    # restPool = range(1, 11)

    # for i, e in enumerate(restPool):
    # print e
    # print s.canWin([], [e], restPool[:i]+restPool[i+1:], 40-e)

    # print s.canWin([], [1], range(2, 11), 39)
    print s.canWin([1], [2], range(3, 11), 37)

    restPool= range(3, 11)
    for i, e in enumerate(restPool):
        print e
        print s.canWin([2], [1, e], restPool[:i]+restPool[i+1:], 37-e)


if __name__ == '__main__':
    main()
