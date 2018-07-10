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
    def canWin(self, restPool, total):
        if total <= max(restPool):
            return True

        r = self.visited.get(restPool)
        if r is not None:
            return r

        for i, e in enumerate(restPool):
            t = tuple(restPool[:i]+restPool[i+1:])
            r = self.visited.get(t)
            if r is False:
                self.visited[restPool] = True
                return True
            if r is True:
                continue

            if not self.canWin(t, total-e):
                self.visited[restPool] = True
                return True
        self.visited[restPool] = False
        return False

    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        >>> s = Solution()
        >>> s.canIWin(2, 10)
        False
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
        if maxChoosableInteger*(1+maxChoosableInteger)/2 < desiredTotal:
            return False
        if maxChoosableInteger*(1+maxChoosableInteger)/2 == desiredTotal:
            return maxChoosableInteger % 2 == 1
        self.visited = {}
        return self.canWin(tuple(range(maxChoosableInteger, 0 , -1)), desiredTotal)


def main():
    s = Solution()
    print s.canIWin(19, 190)


if __name__ == '__main__':
    main()
