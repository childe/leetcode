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
        n = len(parents)

        children = [[] for _ in parents]
        for i, p in enumerate(parents):
            if p != -1:
                children[p].append(i)

        # print(f"{children=}")

        max_count, ans = 0, 0
        step = 0

        def postOrderVisit(node):
            nonlocal step
            step += 1
            nonlocal max_count, ans

            count, r = 1, 1
            for c in children[node]:
                v = postOrderVisit(c)
                count *= v
                r += v
            count *= (n - r) or 1
            if count == max_count:
                ans += 1
            elif count > max_count:
                max_count, ans = count, 1
            return r

        postOrderVisit(0)

        print(f"{step=}")
        return ans


def main():
    s = Solution()
    ans = s.countHighestScoreNodes(parents=[-1, 2, 0, 2, 0])
    print(ans)
    ans = s.countHighestScoreNodes(parents=[-1, 2, 0])
    print(ans)

    parents = eval(open("./testcase").read())
    s = Solution()
    ans = s.countHighestScoreNodes(parents)
    print(ans)

    return


if __name__ == "__main__":
    main()
