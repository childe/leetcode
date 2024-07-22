#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
https://leetcode.cn/problems/candy/
"""


class Solution:
    def candy(self, ratings: list[int]) -> int:
        # max_limit = len(ratings) + 1
        # rst = [1 if e == min_rating else max_limit for e in ratings]
        rst = [1] * len(ratings)

        def dfs(i):
            print(i, rst)
            if i == len(ratings):
                return
            if i == 0:
                return dfs(i + 1)
            if ratings[i] > ratings[i - 1]:
                rst[i] = rst[i - 1] + 1
                return dfs(i + 1)
            if ratings[i] == ratings[i - 1]:
                rst[i] = 1
                return dfs(i + 1)
            rst[i] = min(rst[i - 1] - 1, 1)
            if rst[i] == 0:
                rst[i - 1] += 1
                return dfs(i - 1)
            return dfs(i + 1)

        dfs(1)
        print(rst)
        return sum(rst)


def main():
    s = Solution()
    print(s.candy([1, 0, 2]))  # 5
    print(s.candy([1, 2, 2]))  # 4


if __name__ == "__main__":
    main()
