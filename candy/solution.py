#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
https://leetcode.cn/problems/candy/
"""


class Solution:
    def candy(self, ratings: list[int]) -> int:
        # max_limit = len(ratings) + 1
        # rst = [1 if e == min_rating else max_limit for e in ratings]
        rst = [0] * len(ratings)
        rst[0] = 1

        i = 1
        while i < len(ratings):
            # print(i, rst)
            if i == 0:
                i += 1
                continue
            if ratings[i] > ratings[i - 1]:
                rst[i] = max(rst[i - 1] + 1, rst[i])
                i += 1
            elif ratings[i] == ratings[i - 1]:
                rst[i] = max(1, rst[i])
                i += 1
            else:
                if rst[i] >= rst[i - 1]:
                    rst[i - 1] += 1
                    i -= 1
                else:
                    rst[i] = max(min(rst[i - 1] - 1, 1), rst[i])
                    if rst[i] == 0:
                        rst[i - 1] += 1
                        i -= 1
                    else:
                        i += 1

        # print(rst)
        return sum(rst)


def main():
    s = Solution()
    print(s.candy([1, 2, 87, 87, 87, 2, 1]))  #
    print(s.candy([1, 0, 2]))  # 5
    print(s.candy([1, 2, 2]))  # 4
    print(s.candy([1]))  # 1
    print(s.candy([1, 1, 1]))  # 3
    print(s.candy([2, 2, 1]))  # 4


if __name__ == "__main__":
    main()
