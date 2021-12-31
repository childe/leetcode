#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/push-dominoes/

838. 推多米诺
一行中有 N 张多米诺骨牌，我们将每张多米诺骨牌垂直竖立。

在开始时，我们同时把一些多米诺骨牌向左或向右推。



每过一秒，倒向左边的多米诺骨牌会推动其左侧相邻的多米诺骨牌。

同样地，倒向右边的多米诺骨牌也会推动竖立在其右侧的相邻多米诺骨牌。

如果同时有多米诺骨牌落在一张垂直竖立的多米诺骨牌的两边，由于受力平衡， 该骨牌仍然保持不变。

就这个问题而言，我们会认为正在下降的多米诺骨牌不会对其它正在下降或已经下降的多米诺骨牌施加额外的力。

给定表示初始状态的字符串 "S" 。如果第 i 张多米诺骨牌被推向左边，则 S[i] = 'L'；如果第 i 张多米诺骨牌被推向右边，则 S[i] = 'R'；如果第 i 张多米诺骨牌没有被推动，则 S[i] = '.'。

返回表示最终状态的字符串。

示例 1：

输入：".L.R...LR..L.."
输出："LL.RR.LLRRLL.."
示例 2：

输入："RR.L"
输出："RR.L"
说明：第一张多米诺骨牌没有给第二张施加额外的力。
提示：

0 <= N <= 10^5
表示多米诺骨牌状态的字符串只含有 'L'，'R'; 以及 '.';
"""


class Solution:
    def convert(self, i, j, dominoes):
        if dominoes[i] == "L":
            if dominoes[j] == "L":  # L..L
                dominoes[i : 1 + j] = ["L"] * len(dominoes[i : 1 + j])
            return
        if dominoes[j] == "R":  # R..R
            dominoes[i : 1 + j] = ["R"] * len(dominoes[i : 1 + j])
        if dominoes[j] == "L":  # R..L
            dominoes[i : (i + j + 1) // 2] = ["R"] * len(dominoes[i : (i + j + 1) // 2])
            dominoes[(i + j) // 2 + 1 : j + 1] = ["L"] * len(
                dominoes[(i + j) // 2 + 1 : j + 1]
            )

    def pushDominoes(self, dominoes: str) -> str:
        """
        >>> s = Solution()
        >>> s.pushDominoes(".L.R...LR..L..")
        'LL.RR.LLRRLL..'
        >>> s.pushDominoes("RR.L")
        'RR.L'
        """
        dominoes = "L" + dominoes + "R"
        i, j, l = 0, 0, len(dominoes)
        dominoesList = list(dominoes)
        while j < l:
            while dominoesList[j] == ".":
                j += 1
            # print(i, j, dominoes[i : j + 1])
            self.convert(i, j, dominoesList)
            # print("".join(dominoesList), len(dominoesList))
            i, j = j, j + 1
        return "".join(dominoesList[1:-1])
