#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
https://leetcode.cn/problems/trapping-rain-water/
"""


class Solution:
    def trap(self, height: list[int]) -> int:
        # print(height)
        ans = 0
        p = 0
        i = 0
        while i != len(height) - 1:
            for i in range(p + 1, len(height)):
                if height[i] >= height[p]:
                    ans += height[p] * (i - p - 1) - sum(height[p + 1 : i])
                    p = i
                    break
        if p == len(height) - 1:
            return ans
        return ans + self.trap(height[p:][::-1])


def main():
    s = Solution()
    height = [1, 0, 2, 0, 1]
    print(s.trap(height), 2)

    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(s.trap(height), 6)

    height = [4, 2, 0, 3, 2, 5]
    print(s.trap(height), 9)


if __name__ == "__main__":
    main()
