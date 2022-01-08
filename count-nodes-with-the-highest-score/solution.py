#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/count-nodes-with-the-highest-score/
"""

from functools import reduce


class Solution:
    def countHighestScoreNodes(self, parents: list[int]) -> int:
        """
        >>> s = Solution()
        >>> s.countHighestScoreNodes(parents = [-1,2,0,2,0])
        3
        >>> s.countHighestScoreNodes(parents = [-1,2,0])
        2
        """
        children = []
        for _ in parents:
            children.append([])

        for i, p in enumerate(parents):
            if p != -1:
                children[p].append(i)
        # print(f"{children=}")
        # print(len(children))

        # init childrenCount to [{left:Count, right:Count} ...]
        childrenCount = [{}] * len(parents)
        for i, _ in enumerate(children):
            childrenCount[i] = dict()

        ## filll childrenCount from down to up
        for i, c in enumerate(children):
            # print(f"{i=}")
            if c == []:
                p, childeNode = parents[i], i
                while p != -1:
                    childrenCount[p][childeNode] = 1 + sum(
                        childrenCount[childeNode].values()
                    )
                    if len(children[p]) != len(childrenCount[p]):
                        break
                    p, childeNode = parents[p], p

        # print(f"{childrenCount=}")

        totalCount = len(parents)
        removed = []  # 删除一个节点之后，分出来的所有树的 Node 数量
        for i, c in enumerate(childrenCount):
            removed.append(list(c.values()))
            remainingCount = totalCount - sum(c.values()) - 1
            if remainingCount > 0:
                removed[i].append(remainingCount)

        # print(f"{removed=}")

        r = [reduce(lambda x, y: x * y, e, 1) for e in removed]
        return r.count(max(r))


def main():
    parents = eval(open("./testcase").read())
    print(len(parents))
    s = Solution()
    s.countHighestScoreNodes(parents)


if __name__ == "__main__":
    main()
