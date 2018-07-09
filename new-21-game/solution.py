#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/new-21-game/description/


Alice plays the following game, loosely based on the card game "21".

Alice starts with 0 points, and draws numbers while she has less than K points.  During each draw, she gains an integer number of points randomly from the range [1, W], where W is an integer.  Each draw is independent and the outcomes have equal probabilities.

Alice stops drawing numbers when she gets K or more points.  What is the probability that she has N or less points?

Example 1:

Input: N = 10, K = 1, W = 10
Output: 1.00000
Explanation:  Alice gets a single card, then stops.
Example 2:

Input: N = 6, K = 1, W = 10
Output: 0.60000
Explanation:  Alice gets a single card, then stops.
In 6 out of W = 10 possibilities, she is at or below N = 6 points.
Example 3:

Input: N = 21, K = 17, W = 10
Output: 0.73278
Note:

0 <= K <= N <= 10000
1 <= W <= 10000
Answers will be accepted as correct if they are within 10^-5 of the correct answer.
The judging time limit has been reduced for this question.

"""


class Solution(object):
    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        if N - K >= W-1:
            return 1
        if N < K:
            return 0

        if N == 0:
            return 1

        # p[i]是i这个点可以被到达的概率, 比如W=3的情况下, p[1]=1/3, p[2]=1/3*1/3 + 1*1/3
        p = [0] * (N+1)
        p[0], p[1] = 1.0, 1.0/W
        for i in range(2, N+1):
            if i-W-1 < 0:
                p[i] = p[i-1] + p[i-1]/W
            else:
                p[i] = (p[i-1] - p[i-W-1])/W+p[i-1]

        # for idx, e in enumerate(p):
            # print idx, e

        rst = 1.0
        for i in range(max(0, N-W+1), K):
            rst -= p[i] * (W-(N-i))/W

        return rst


def main():
    import time
    s1 = time.time()
    s = Solution()
    # print s.new21Game(21, 17, 10)
    # print s.new21Game(12, 10, 4)

    print s.new21Game(10, 10, 3)

    # print s.new21Game(0, 0, 3)

    # print s.new21Game(1, 0, 5)

    # print s.new21Game(6, 1, 10)

    print s.new21Game(9811, 8776, 1096)
    print s.new21Game(8954, 8556, 506)
    print time.time() - s1


if __name__ == '__main__':
    main()
