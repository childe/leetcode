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
    def __init__(self):
        self.expenditures = []

    def blockCount(self, houses):
        """
        >>> s = Solution()
        >>> s.blockCount([3,1,2,3])
        4
        >>> s.blockCount([1,1,1,1])
        1
        >>> s.blockCount([1,1,2,1])
        3
        """
        rst = 0
        pre = None
        for n in houses:
            if n == pre:
                continue
            rst += 1
            pre = n

        return rst

    def noZero(self, houses):
        return all([e != 0 for e in houses])

    def reMinCost(self, houses, cost, m, n, target, zeroCount, expenditure):
        """
        :type houses: List[int]
        :type cost: List[List[int]]
        :type m: int
        :type n: int
        :type target: int
        :rtype: int
        """
        if zeroCount == 0:
            if self.blockCount(houses) != target:
                return -1
            return expenditure

        for i, h in enumerate(houses):
            if h == 0:
                for j, c in enumerate(cost[i]):
                    r = self.reMinCost(houses[:i]+[j+1] + houses[i+1:], cost, m, n, target, zeroCount-1, expenditure+c)
                    if r != -1:
                        self.expenditures.append(r)

        if self.expenditures:
            return min(self.expenditures)
        return -1

    def minCost(self, houses, cost, m, n, target):
        zeroCount = sum([h == 0 for h in houses])
        return self.reMinCost(houses, cost, m, n, target, zeroCount, 0)


def main():
    s = Solution()

    houses = [0, 2, 1, 2, 0]
    cost = [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]]
    m = 5
    n = 2
    target = 3
    ans = s.minCost(houses, cost, m, n, target)
    print(ans)
    assert ans == 11

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
