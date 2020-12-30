# -*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/paint-house-iii/

在一个小城市里，有 m 个房子排成一排，你需要给每个房子涂上 n 种颜色之一（颜色编号为 1 到 n ）。有的房子去年夏天已经涂过颜色了，所以这些房子不需要被重新涂色。

我们将连续相同颜色尽可能多的房子称为一个街区。（比方说 houses = [1,2,2,3,3,2,1,1] ，它包含 5 个街区  [{1}, {2,2}, {3,3}, {2}, {1,1}] 。）

给你一个数组 houses ，一个 m * n 的矩阵 cost 和一个整数 target ，其中：

houses[i]：是第 i 个房子的颜色，0 表示这个房子还没有被涂色。
cost[i][j]：是将第 i 个房子涂成颜色 j+1 的花费。
请你返回房子涂色方案的最小总花费，使得每个房子都被涂色后，恰好组成 target 个街区。如果没有可用的涂色方案，请返回 -1 。


# 示例 1：

```
输入：houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
输出：9
解释：房子涂色方案为 [1,2,2,1,1]
此方案包含 target = 3 个街区，分别是 [{1}, {2,2}, {1,1}]。
涂色的总花费为 (1 + 1 + 1 + 1 + 5) = 9。
```

# 示例 2：

```
输入：houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
输出：11
解释：有的房子已经被涂色了，在此基础上涂色方案为 [2,2,1,2,2]
此方案包含 target = 3 个街区，分别是 [{2,2}, {1}, {2,2}]。
给第一个和最后一个房子涂色的花费为 (10 + 1) = 11。
```

# 示例 3：

```
输入：houses = [0,0,0,0,0], cost = [[1,10],[10,1],[1,10],[10,1],[1,10]], m = 5, n = 2, target = 5
输出：5
```

# 示例 4：

```
输入：houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], m = 4, n = 3, target = 3
输出：-1
解释：房子已经被涂色并组成了 4 个街区，分别是 [{3},{1},{2},{3}] ，无法形成 target = 3 个街区。
```
"""


class Solution(object):
    def minCost(self, houses, cost, m, n, target):
        # dp[i][j] 意思是, 前 i 个 house, 刷成 target = j 街区的所有可能的 [color[i], cost]
        dp = [[None] * (m + 1)] * (target + 1)

        # init
        dp[0][0] = [None, 0]

        ## m 个 house 刷成 0 个 target ,  可能的 (color,cost) 组合为空
        for i in range(1, target + 1):
            dp[0][i] = []

        ## 0 house 刷 0 block, cost = 0.  可能的 (color,cost) 组合为空
        for i in range(1, target + 1):
            dp[i][0] = []

        for row in dp:
            print(row)

        for i in range(1, m + 1):
            for j in range(1, target + 1):
                dp[i - 1][j - 1] + cost[i]


def main():
    import json

    s = Solution()

    # lines = open("./input").readlines()
    # houses = json.loads(lines[0].strip())
    # cost = json.loads(lines[1].strip())
    # m = int(lines[2].strip())
    # n = int(lines[3].strip())
    # target = int(lines[4].strip())
    # ans = s.minCost(houses, cost, m, n, target)
    # print(ans)
    # assert ans == 11
    # return

    houses = [0, 2, 1, 2, 0]
    cost = [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]]
    m = 5
    n = 2
    target = 3
    ans = s.minCost(houses, cost, m, n, target)
    print(ans)
    assert ans == 11
    return

    houses = [0, 0, 0, 0, 0]
    cost = [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]]
    m = 5
    n = 2
    target = 3
    ans = s.minCost(houses, cost, m, n, target)
    print(ans)
    assert ans == 9

    houses = [3, 1, 2, 3]
    cost = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]
    m = 4
    n = 3
    target = 3
    ans = s.minCost(houses, cost, m, n, target)
    print(ans)
    assert ans == -1


if __name__ == "__main__":
    main()
