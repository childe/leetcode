# -*- coding: utf-8 -*-

import math


class Solution:
    def numSquares(self, n: int) -> int:
        q = [(0, n)]
        visited = {n: 0}
        while q:
            # print(q)
            # print(visited)
            step, num = q.pop()
            # print('  ', step, num)
            for i in range(int(math.sqrt(num)//1), 0, -1):
                square = i**2
                if square == num:
                    return step + 1
                d = num - square
                if d not in visited:
                    visited[d] = step+1
                    q.insert(0, (step+1, d))


def main():
    s = Solution()

    for n, output in zip([7168, 72, 12, 13], [4, 2, 3, 2]):
        a = s.numSquares(n)
        print(n, a, output)
        assert(a == output)


if __name__ == '__main__':
    main()
