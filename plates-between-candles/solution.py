#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
https://leetcode-cn.com/problems/plates-between-candles/

There is a long table with a line of plates and candles arranged on top of it. You are given a 0-indexed string s consisting of characters '*' and '|' only, where a '*' represents a plate and a '|' represents a candle.

You are also given a 0-indexed 2D integer array queries where queries[i] = [lefti, righti] denotes the substring s[lefti...righti] (inclusive). For each query, you need to find the number of plates between candles that are in the substring. A plate is considered between candles if there is at least one candle to its left and at least one candle to its right in the substring.

For example, s = "||**||**|*", and a query [3, 8] denotes the substring "*||**|". The number of plates between candles in this substring is 2, as each of the two plates has at least one candle in the substring to its left and right.
Return an integer array answer where answer[i] is the answer to the ith query.

 

Example 1:


Input: s = "**|**|***|", queries = [[2,5],[5,9]]
Output: [2,3]
Explanation:
- queries[0] has two plates between candles.
- queries[1] has three plates between candles.

Example 2:


Input: s = "***|**|*****|**||**|*", queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]
Output: [9,0,0,0,0]
Explanation:
- queries[0] has nine plates between candles.
- The other queries have zero plates between candles.
 

Constraints:

3 <= s.length <= 10^5
s consists of '*' and '|' characters.
1 <= queries.length <= 10^5
queries[i].length == 2
0 <= lefti <= righti < s.length
"""


class Solution:
    def platesBetweenCandles(self, s: str, queries: list[list[int]]) -> list[int]:
        """
        >>> s = Solution()
        >>> s.platesBetweenCandles("**|**|***|", [[2,5],[5,9]])
        [2, 3]
        >>> s.platesBetweenCandles("***|**|*****|**||**|*", [[1,17],[4,5],[14,17],[5,11],[15,16]])
        [9, 0, 0, 0, 0]
        """
        length = len(s)

        # left[i]：第 i 个盘子左边的离它最近的蜡烛，如果是 -1，说明它左边没有蜡烛
        most_left, left = -1, []
        for i, c in enumerate(s):
            if c == "|":
                most_left = i
            left.append(most_left)

        most_right, right = length, [length] * length
        for i in range(length - 1, -1, -1):
            if s[i] == "|":
                most_right = i
            right[i] = most_right

        # left_plate_count[i]: 第 i 个蜡烛左边有多少个盘子
        left_plate_count = [0] * length
        count = 0
        for i, c in enumerate(s):
            if c == "*":
                count += 1
            else:
                left_plate_count[i] = count

        ans = []
        for i, q in enumerate(queries):
            # print(f"{i}/{len(queries)}")
            # print(f"{q=}")
            l, r = right[q[0]], left[q[1]]
            if l >= r:
                count = 0
            else:
                count = left_plate_count[r] - left_plate_count[l]
            # print(l, r, count)
            ans.append(count)

        return ans
