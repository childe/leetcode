# -*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/

You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0)
and sell on day 6 (price = 3), profit = 3-0 = 3.
 

Constraints:

0 <= k <= 100
0 <= prices.length <= 1000
0 <= prices[i] <= 1000
"""


class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k == 0:
            return 0
        if not prices[1:]:
            return 0

        tuples = self.findtuples(prices)

        while len(tuples) > k:
            tuples = self.decrease(tuples)

        return sum(e[1] - e[0] for e in tuples)

    def findtuples(self, prices):
        print("findtuples", prices)

        tuples = []
        t = [prices[0], -1]
        for p in prices[1:]:
            if t[1] != -1:
                if p < t[1]:
                    tuples.append(t)
                    t = [p, -1]
                    continue
                t[1] = p
            else:
                if p <= t[0]:
                    t[0] = p
                else:
                    t[1] = p

        if t[0] != -1 and t[1] != -1:
            tuples.append(t)
        print("tuples", tuples)
        return tuples

    def decrease(self, tuples):
        print("decrease tuples", tuples)
        v1 = []
        for i, t in enumerate(tuples[:-1]):
            v1.append(t[1] - tuples[i + 1][0])
        v2 = [e[1] - e[0] for e in tuples]
        if min(v1) < min(v2):
            i = v1.index(min(v1))
            t = [tuples[i][0], tuples[i + 1][1]]
            n = tuples[:i] + [t] + tuples[i + 2 :]
        else:
            i = v2.index(min(v2))
            n = tuples[:i] + tuples[i + 1 :]

        print("new tuples", n)
        return n

    def decrease2(self, tuples):
        print("decrease tuples", tuples)
        v = []
        for i, t in enumerate(tuples[:-1]):
            v.append(t[1] - tuples[i + 1][0])

        i = v.index(min(v))
        t = [tuples[i][0], tuples[i + 1][1]]

        v = [
            t[1] - t[0],
            tuples[i][1] - tuples[i][0],
            tuples[i + 1][1] - tuples[i + 1][0],
        ]
        j = v.index(max(v))
        if j != 0:
            t = tuples[i + j - 1]
        n = tuples[:i] + [t] + tuples[i + 2 :]
        print("new tuples", n)
        return n


def main():
    s = Solution()
    k = 0
    prices = [1, 3]
    p = s.maxProfit(k, prices)
    print(p)
    assert p == 0

    k = 2
    prices = [8, 6, 4, 3, 3, 2, 3, 5, 8, 3, 8, 2, 6]
    p = s.maxProfit(k, prices)
    print(p)
    assert p == 11

    k = 1
    prices = [6, 1, 6, 4, 3, 0, 2]
    p = s.maxProfit(k, prices)
    print(p)
    assert p == 5

    k = 2
    prices = [1, 2]
    p = s.maxProfit(k, prices)
    print(p)
    assert p == 1

    k = 2
    prices = [2, 1]
    p = s.maxProfit(k, prices)
    print(p)
    assert p == 0

    k = 2
    prices = []
    p = s.maxProfit(k, prices)
    print(p)
    assert p == 0

    k = 2
    prices = [2]
    p = s.maxProfit(k, prices)
    print(p)
    assert p == 0

    k = 2
    prices = [2, 4, 1]
    p = s.maxProfit(k, prices)
    print(p)
    assert p == 2

    prices = [3, 2, 6, 5, 0, 3]
    k = 2
    p = s.maxProfit(k, prices)
    print(p)
    assert p == 7

    k = 2
    prices = [3, 3, 5, 0, 0, 3, 1, 4]
    p = s.maxProfit(k, prices)
    print(p)
    assert p == 6


if __name__ == "__main__":
    main()
