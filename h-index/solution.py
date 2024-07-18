# -*- coding: utf-8 -*-

"""
https://leetcode.cn/problems/h-index/description/
"""

import math


class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort()
        sq = math.floor(math.sqrt(sum(citations)))
        for i in range(min(sq, len(citations)), -1, -1):
            if citations[-i] >= i:
                return i
        return 0 if max(citations) == 0 else 1


def main():
    solution = Solution()

    citations = [1, 2, 100]
    print(solution.hIndex(citations), solution.hIndex(citations) == 2)

    citations = [11, 12]
    print(solution.hIndex(citations), solution.hIndex(citations) == 2)

    citations = [100]
    print(solution.hIndex(citations) == 1)

    citations = [0, 1, 3, 5, 6]
    print(solution.hIndex(citations) == 3)

    ca = [1, 3, 1]
    print(solution.hIndex(ca) == 1)

    ca = [1]
    print(solution.hIndex(ca) == 1)


if __name__ == "__main__":
    main()
