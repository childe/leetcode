#!/usr/bin/env python3
"""
https://leetcode.cn/problems/random-point-in-non-overlapping-rectangles/

497. 非重叠矩形中的随机点
给定一个由非重叠的轴对齐矩形的数组 rects ，其中 rects[i] = [ai, bi, xi, yi] 表示 (ai, bi) 是第 i 个矩形的左下角点，(xi, yi) 是第 i 个矩形的右上角点。设计一个算法来随机挑选一个被某一矩形覆盖的整数点。矩形周长上的点也算做是被矩形覆盖。所有满足要求的点必须等概率被返回。

在给定的矩形覆盖的空间内的任何整数点都有可能被返回。

请注意 ，整数点是具有整数坐标的点。

实现 Solution 类:

Solution(int[][] rects) 用给定的矩形数组 rects 初始化对象。
int[] pick() 返回一个随机的整数点 [u, v] 在给定的矩形所覆盖的空间内。
 

示例 1：



输入: 
["Solution", "pick", "pick", "pick", "pick", "pick"]
[[[[-2, -2, 1, 1], [2, 2, 4, 6]]], [], [], [], [], []]
输出: 
[null, [1, -2], [1, -1], [-1, -2], [-2, -2], [0, 0]]

解释：
Solution solution = new Solution([[-2, -2, 1, 1], [2, 2, 4, 6]]);
solution.pick(); // 返回 [1, -2]
solution.pick(); // 返回 [1, -1]
solution.pick(); // 返回 [-1, -2]
solution.pick(); // 返回 [-2, -2]
solution.pick(); // 返回 [0, 0]
 

提示：

1 <= rects.length <= 100
rects[i].length == 4
-10^9 <= ai < xi <= 10^9
-10^9 <= bi < yi <= 10^9
xi - ai <= 2000
yi - bi <= 2000
所有的矩形不重叠。
pick 最多被调用 104 次。
"""

import random


class Solution:
    def get_point_count_in_one_rectangle(self, rect: list[int]) -> int:
        return (1 + rect[3] - rect[1]) * (1 + rect[2] - rect[0])

    def find_target_idx(self, target: int) -> int:
        # for i, n in enumerate(self.point_count_array):
        # if target <= n:
        # return i
        # return -1

        s, e = 0, len(self.point_count_array) - 1
        while s < e:
            m = (s + e) // 2
            if target > self.point_count_array[m]:
                s = m + 1
            else:
                e = m

        return s

    def __init__(self, rects: list[list[int]]):
        self.rects = rects
        self.point_count_array = []
        s = 0
        for rect in rects:
            c = self.get_point_count_in_one_rectangle(rect)
            s += c
            self.point_count_array.append(s)

    def pick(self) -> list[int]:
        picked = random.randint(1, self.point_count_array[-1])
        idx = self.find_target_idx(picked)
        rect = self.rects[idx]

        x = random.randint(rect[0], rect[2])
        y = random.randint(rect[1], rect[3])
        return [x, y]
